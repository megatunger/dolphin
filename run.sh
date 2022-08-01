sudo apt install git

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

source $HOME/.poetry/env

poetry install

python3 manage.py migrate

python3 manage.py runserver 8011