willtalkback
============

[![Build Status](https://circleci.com/gh/jessamynsmith/willtalkback.svg?style=shield)](https://circleci.com/gh/jessamynsmith/willtalkback)
[![Coverage Status](https://coveralls.io/repos/jessamynsmith/willtalkback/badge.svg?branch=master)](https://coveralls.io/r/jessamynsmith/willtalkback?branch=master)

will plugin for talkbackbot
This was just a proof of concept; the real code lives at:
https://github.com/skoczen/will/blob/master/will/plugins/friendly/talk_back.py


Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/willtalkback.git

Create a virtualenv and install dependencies:

    mkvirtualenv willtalkback
    pip install -r requirements/development.txt

Run tests and view coverage:

    coverage run -m nose
    coverage report

Check code style:

    flake8
