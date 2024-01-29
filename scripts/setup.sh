#!/bin/bash

sudo yum install pip -y
sudo yum install git -y
cd ~
git clone https://github.com/tpoombavai/Cloud_Computing_Assignment_2.git
cd Cloud_Computing_Assignment_2/
pip install -r requirements.txt
nohup ./start.sh &

