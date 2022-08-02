#!/bin/bash

cd /usr/local/src/dolphin

source ./.venv/bin/activate

export SYNAPSE_SERVER=http://0.0.0.0:8008

export ADMIN_TOKEN=syt_YWRtaW4_VCTyHEmfytfkCxhHlRhD_16ZG4e

export WIDGET_URLS='["uCall","https://google.com","uCall 2","http://localhost:3000"]'

python3 manage.py migrate

python3 manage.py runserver 8011