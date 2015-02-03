willtalkback
============

will plugin for talkbackbot


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
