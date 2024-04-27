#!/usr/bin/python3
"""An index file"""
# api/v1/views/index.py
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity


# Define route
@app_views.route('/status', methods=['GET'])
def get_status():
    """W method call when /status is accessed"""
    return jsonify({"status": "OK"})


# Define route to retrieve number of objects by type
@app_views.route('/stats', methods=['GET'])
def get_stats():
    stats = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    for cls_name in classes:
        count = storage.count(eval(cls_name))
        stats[cls_name] = count
        return jsonify(stats)
