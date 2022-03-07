from flask import request, jsonify, flash, redirect, url_for
from flask_restx import Api, Resource, fields, Namespace

from db import db


decks_namespace = Namespace('api/v1/decks', description='decksのエンドポイント')


@decks_namespace.route('/')
class Decks(Resource):
    def get(self):
        decks = db.decks.find_one()

        return jsonify(decks)

    def post(self):
        b = request.get_json()
        db.decks.insert_one({"name": b.get('name'), "description": b.get('description')})
        response = {
            "deck": b.get('name'),
            "card": b.get('description')
        }

        return jsonify(response)