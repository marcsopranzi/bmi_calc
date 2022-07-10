#!/bin/bash

echo "Installing python vevn "
sudo apt install python3.10-venv

echo "Installing python pip"
sudo apt install python3-pip

echo "Installing venv"
python3 -m venv venv_bmi_calc

echo "Activating venv"
source ./venv_bmi_calc/bin/activate

echo "Install dependencies"
pip install "pytest==7.1.2" "numpy==1.23.0" "pandas" "math" "sqlite3"

echo "Pip upgrade"
pip install --upgrade pip