from flask import Flask
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)

Bootstrap = Bootstrap(app)

from app import views