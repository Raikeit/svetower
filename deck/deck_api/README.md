# Get Started
## Create Python Env. (For Linux)

    $ cd deck/deck_api
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install --upgrade pip
    $ pip isntall -r requirements.txt

## Mongodb

    $ sudo docker pull mongo:3.6.1-jessie
    $ sudo docker run --name my-mongo -d -p 27017:27017 mongo:3.6.1-jessie

## Run

    $ flask run

Open http://127.0.0.1:5000/

# Setup Cardlist

    $ python setCards.py --commit raw/sd_neutral.json
    $ python setCards.py --commit raw/sd01_elf.json

## check data

    $ flask run

Open http://127.0.0.1:5000/api/v1/cards/