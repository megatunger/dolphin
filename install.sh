#!/bin/bash

sudo apt install git

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

export PATH="$HOME/.poetry/bin:$PATH"

poetry config virtualenvs.in-project true

poetry install

x=$(pwd)

cp -R "$x" /usr/local/src/dolphin

sudo chmod +x /usr/local/src/dolphin/run.sh

rm -rf /lib/systemd/system/dolphin.service

sudo cp dolphin.service /lib/systemd/system/dolphin.service

sudo systemctl daemon-reload

sudo systemctl stop dolphin.service

sudo systemctl start dolphin.service