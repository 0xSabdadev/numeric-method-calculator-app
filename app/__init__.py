from flask import Flask

app = Flask(__name__)

from app import views
from .utils import filters

# app.config.from_object("config.Config")