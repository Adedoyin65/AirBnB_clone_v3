#!/usr/bin/python3
"""An init file"""
# api/v1/views/__init__.py
from flask import Blueprint

# Create Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
