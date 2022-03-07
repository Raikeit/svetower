import os

from flask import Flask, current_app, g
from flask_pymongo import PyMongo
from flask.json import JSONEncoder
from flask_cors import CORS

from werkzeug.local import LocalProxy
from bson import json_util, ObjectId
from datetime import datetime, timedelta

from view import create_contacts


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.json_encoder = MongoJsonEncoder

    blueprint = create_contacts()
    app.register_blueprint(blueprint)

    return app

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db

    return db

db = LocalProxy(get_db)