
# My Docker Place

My Dockerplace is a simple web app to control your container applications.

## Requirements

All your docker services must reside under a single folder. This folder will be scanned for services.
Inside this folder, you must place a `Makefile`. The app will read it to find the tasks you can perform on that service.

## Configuration

Change the folder in settings.py to the one in your machine.

## Running

for the non-dockerized version, 

    python app.py
