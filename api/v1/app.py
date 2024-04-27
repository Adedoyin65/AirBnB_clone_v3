#!/usr/bin/python3
"""An api module"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views)


# Teardown app context to close storage
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

# Handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    # Run Flask server
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
