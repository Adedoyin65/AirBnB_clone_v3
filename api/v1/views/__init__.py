#!/usr/bin/python3
"""An init file"""
# Import views
from api.v1.views.index import *
# api/v1/views/__init__.py
from flask import Blueprint

# Create Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
