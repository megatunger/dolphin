#!/bin/bash

cd /usr/local/src/dolphin

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

printenv

export PATH="$HOME/.poetry/bin:$PATH"

poetry install

poetry run python3 manage.py migrate

poetry run python3 manage.py runserver 8011