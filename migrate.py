import json
from run import db
import models


# Загружаем данные в json

def load_data(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)


    return json_data

# Загружаем json спиок с users

def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)

    print(models.User.get(1).to_dict)

# Загружаем json спиок с orders

def load_orders(filename):
    orders = load_data(filename)

    for order in orders:
        new_order = models.Offer(**order)
        db.session.add(new_order)

    print(models.Order.get(1).to_dict)

# Загружаем json спиок с offers

def load_offers(filename):
    offers = load_data(filename)

    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)

print(models.Offer.get(1).to_dict)
