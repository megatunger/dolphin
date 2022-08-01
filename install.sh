sudo apt install git

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

x=$(pwd)

cp -R "$x" /usr/local/src/dolphin

sudo cp dolphin.service /lib/systemd/system/dolphin.service

sudo systemctl daemon-reload

sudo systemctl stop dolphin.service

sudo systemctl start dolphin.service