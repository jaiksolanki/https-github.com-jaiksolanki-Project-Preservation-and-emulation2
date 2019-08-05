#!/usr/bin/env bash

sudo docker build -t beproject .
sudo docker run -p 5000:5000 --name beproject beproject