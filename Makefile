help:
	@echo "Welcome to your Docker Place"
	@echo ""
	@echo "run     					- Execute the service in dev mode"
	@echo "install-global 	- Install the requirements, globally on your system"
	@echo "install-venv 		- Install the requirements, Using VirtualEnv in the local folder"
	@echo "test    					- run the tests"
	@echo ""

run:
	python app.py

install-global:
	sudo pip install -r requirements.txt


install_venv:
	virtualenv ENV; source bin/activate; pip install -r requirements.txt

test:
	nosetests

Mayus:
	@echo "deleteme"

1number:
	@echo "deleteme"

