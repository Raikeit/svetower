from flask import Blueprint, blueprints
from flask_restx import Api

def create_contacts():
    blueprint = Blueprint("contacts_api", __name__)
    contacts_api = Api(
        blueprint,
        title='AIMUS-ML API',
        version='0.1',
        description=''
    )

    from .decks import decks_namespace
    from .cards import cards_namespace
    contacts_api.add_namespace(decks_namespace)
    contacts_api.add_namespace(cards_namespace)

    return blueprint