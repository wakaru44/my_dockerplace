
# My Docker Place


My Dockerplace is a simple UI to control your [Docker](https://www.docker.com/)  containers (locally).

It's in early alpha development, as a sort of "experiment" with docker.

It's a simple web, that runs locally backed by python. You start from a simple "desktop":

![An example of the desktop, with your docker services on display](https://raw.githubusercontent.com/wakaru44/my_dockerplace/master/doc/img/screen_desktop_01.png)

And see the output on the web

![An example (with fake data) of how the output would look like](https://raw.githubusercontent.com/wakaru44/my_dockerplace/master/doc/img/screen_console_01.png)

## TL;DR - Quickstart

You will need Python >2.7 
clone the repo

    git clone https://github.com/wakaru44/my_dockerplace.git
    cd my_dockerplace

customize your docker home folder (where your containers live)

    vim settings.py

install dependencies and run the app.
To install with your "system" python:

    make install-global && make run

To install with virtualenv (you will need it set up)

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


# Some Future Feats and Features 

- do some previous validation of the destination folder, docker setup.

- allow the app to shut down itself

- add a link to the start menu/the system apps 
