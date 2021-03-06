from db import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

app = create_app()
app.config['DEBUG'] = True
app.config['MONGO_URI'] = "mongodb://localhost:27017/cards"

from view.decks import *
from view.cards import *

if __name__ == "__main__":
    app.run(debug=True)
