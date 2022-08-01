sudo apt install git

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

sudo cp dolphin.service /lib/systemd/system/dolphin.service

sudo systemctl daemon-reload

sudo systemctl enable dolphin.service