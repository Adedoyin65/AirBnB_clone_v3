#!/usr/bin/python3
"""An index file"""
# api/v1/views/index.py
from api.v1.views import app_views
from flask import jsonify


# Define route
@app_views.route('/status', methods=['GET'])
def get_status():
    """W method call when /status is accessed"""
    return jsonify({"status": "OK"})
