from flask import request, jsonify, flash, redirect, url_for
from flask_restx import Api, Resource, fields, Namespace

from db import db


cards_namespace = Namespace('api/v1/cards', description='cardsのエンドポイント')


@cards_namespace.route('/')
class Cards(Resource):
    def get(self):
        cards = db.cards.find()
        return jsonify([d for d in cards])

@cards_namespace.route('/<string:key>/<string:value>/')
class CardsFind(Resource):
    def get(self, key: str, value: str):
        cards = db.cards.find({
            key: value
        })
        return jsonify([d for d in cards])