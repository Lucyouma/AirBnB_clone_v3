#!/usr/bin/python3
"""
Flask application imlementation
"""
from models import storage
from os import environ
from flask import Flask, make_response, render_template, jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """
    closes storage
    """
    storage.close()


if __name__ == "__main__":
    """
    main implementation
    """
    host = environ.get('HNBN_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', '500')

    app.run(host=host, port=port, threaded=True)
