cd /usr/local/src/dolphin

source $HOME/.poetry/env

poetry install

poetry run python3 manage.py migrate

poetry run python3 manage.py runserver 8011