#!/bin/bash

cd /opt/RemoveBackground

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade pathlib
python3 -m pip install --upgrade rembg

# make folders
mkdir -p ~/RemoveBackground
mkdir /opt/RemoveBackground/images

# run the script
python3 /opt/RemoveBackground/src/RemoveBackground.py

sleep 5m

deactivate

rm -r venv
