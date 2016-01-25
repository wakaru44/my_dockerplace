help:
	@echo "Welcome to your Docker Place"
	@echo ""
	@echo "run     - Execute the service in dev mode"
	@echo "install - Install the requirements"
	@echo "test    - run the tests"
	@echo ""

run:
	python app.py

install:
	sudo pip install -r requirements.txt

test:
	nosetests

Mayus:
	@echo "deleteme"

1number:
	@echo "deleteme"

