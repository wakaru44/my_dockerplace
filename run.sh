#!/bin/bash
APP_HOME="/home/wakaru/workspace/src/python/my_dockerplace"
nohup /usr/bin/python $APP_HOME/app.py 2>&1 | tee -a $APP_HOME/app.$(date +%F).log &
xdg-open http://localhost:8080    
