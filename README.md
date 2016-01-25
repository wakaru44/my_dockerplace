
# My Docker Place

My Dockerplace is a simple web app to control your container applications.

## Requirements

All your docker services must reside under a single folder. This folder will be scanned for services.
Inside this folder, you must place a `Makefile`. The app will read it to find the tasks you can perform on that service.

## Configuration

Change the folder in settings.py to the one in your machine.

## Running

There are tasks ready in a `Makefile`. Just run

    make

to see the available tasks.

## TL;DR - Quickstart

clone the repo

    git clone https://github.com/wakaru44/my_dockerplace.git
    cd my_dockerplace

install dependencies

    make install

run the app

    make run
