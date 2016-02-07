#!/bin/bash
APP_HOME="/home/wakaru/workspace/src/python/my_dockerplace"
cd $APP_HOME
echo "Starting app in $(pwd)" >> $APP_HOME/app.$(date +%F).log 
nohup /usr/bin/python $APP_HOME/app.py 2>&1 | tee -a $APP_HOME/app.$(date +%F).log &
xdg-open "http://localhost:$(grep "PORT=" settings.py | cut -d "=" -f 2)"/
