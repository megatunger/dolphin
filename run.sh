#!/bin/bash

cd /usr/local/src/dolphin

. venv/bin/activate

python3 manage.py migrate

python3 manage.py runserver 8011