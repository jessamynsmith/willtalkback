import logging
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to


class TalkBackPlugin(WillPlugin):

    QUOTES_URL = ("https://underquoted.herokuapp.com/api/v1/quotations/?"
                  "format=json&random=true&limit=1")

    def get_quote(self):
        quote = None
        response = requests.get(self.QUOTES_URL)
        if response.status_code == 200:
            try:
                quote_obj = response.json()['objects'][0]
                quote = u'%s ~ %s' % (quote_obj['text'],
                                      quote_obj['author']['name'])
            except ValueError:
                logging.error(
                    "Response from '%s' could not be decoded as JSON:\n%s"
                    % (self.QUOTES_URL, response))
            except KeyError as e:
                logging.error(
                    "Response from '%s' did not contain field: %s\n%s"
                    % (self.QUOTES_URL, e, response))

        else:
            logging.error("Got an error from '%s': %s\n%s"
                          % (self.QUOTES_URL, response.status_code, response))
        return quote

    @respond_to("that's what she said")
    def talk_back(self, message):
        quote = self.get_quote()
        if quote:
            self.reply(message, quote)
