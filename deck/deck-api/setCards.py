from pymongo import MongoClient
import json
import argparse

def add_cardlist(db, cards: json):
    db.cards.insert_many(cards)

def delete_cardlist_all(db):
    db.cards.drop()

def show_cardlist_all(db):
    data = db.cards.find()
    for d in data:
        print(d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--commit', dest='input_file', type=str, help='json file of cardlist.')
    parser.add_argument('--delete', dest='delete', action='store_true', help='delete all data on database')
    parser.add_argument('--show', dest='show', action='store_true', help='show all data on database')

    args = parser.parse_args()

    with MongoClient("mongodb://localhost:27017/") as client:
        if args.input_file is not None:
            input_file = args.input_file
            with open(input_file, 'r') as f:
                cardlist = json.load(f)

                add_cardlist(client.cards, cardlist)
                show_cardlist_all(client.cards)
        elif args.delete:
            delete_cardlist_all(client.cards)
        else:
            show_cardlist_all(client.cards)