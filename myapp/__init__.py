from flask import Flask
from flaskext.csrf import csrf

app = Flask(__name__)
app.config.from_object('settings')
csrf(app)
from myapp import main

