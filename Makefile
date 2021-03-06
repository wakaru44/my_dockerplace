help:
	@echo "Welcome to your Docker Place"
	@echo ""
	@echo "run     			- Execute the service in dev mode. Stop with Ctrl+C"
	@echo "daemon     			- Run the service like a daemon. Stop with - make stop -"
	@echo "install-global 			- Install the requirements, globally on your system"
	@echo "install-venv 			- Install the requirements, Using VirtualEnv in the local folder"
	@echo "stop				- Kill the application"
	@echo "test    			- run the tests"
	@echo ""

run:
	python app.py

daemon:
	bash run.sh

install-global:
	sudo pip install -r requirements.txt


install-venv:
	virtualenv ENV; source bin/activate; pip install -r requirements.txt

stop:
	pkill -f "my_dockerplace/app.py"

test:
	nosetests

Mayus:
	@echo "deleteme"

1number:
	@echo "deleteme"

