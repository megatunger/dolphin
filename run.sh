curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry install

python manage.py migrate

python manage.py runserver 8011