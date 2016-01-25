
# My Docker Place

My Dockerplace is a simple web app to control your container applications.

![An example of the desktop, with your docker services on display](https://raw.githubusercontent.com/wakaru44/my_dockerplace/master/doc/img/screen_desktop_01.png)
![An example (with fake data) of how the output would look like](https://raw.githubusercontent.com/wakaru44/my_dockerplace/master/doc/img/screen_console_01.png)

## TL;DR - Quickstart

clone the repo

    git clone https://github.com/wakaru44/my_dockerplace.git
    cd my_dockerplace

install dependencies and run the app

    make install && make run

## Requirements

All your docker services must reside under a single folder. This folder will be scanned for services.
Inside this folder, you must place a `Makefile`. The app will read it to find the tasks you can perform on that service.

## Configuration

Change the folder in settings.py to the one in your machine.

## Running

There are tasks ready in a `Makefile`. Just run

    make

to see the available tasks.
