from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Далее код, перенесенный из models

# Описываем класс User

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role  = db.Column(db.String(50))
    phone  = db.Column(db.String(50))

# Описываем класс Offer

class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    last_name = db.Column(db.String(20))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

# Описываем класс Order


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    start_date = db.Column(db.String(200))
    end_date = db.Column(db.String(200))
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

db.create_all()



# Загружаем данные в json

def load_data(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)
    return json_data


# Загружаем json спиок с users

def load_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
    for user in users:
        new_user = User(**elem)
        db.session.add(new_user)
        db.session.commit()

load_users()


# Загружаем json спиок с orders

def load_orders():
    with open('orders.json', 'r', encoding='utf-8') as f:
        orders = json.load(f)
    for order in orders:
        new_order = Order(**elem)
        db.session.add(new_order)
        db.session.commit()

load_orders()



# Загружаем json спиок с offers

def load_offers():
    with open('offers.json', 'r', encoding='utf-8') as f:
        offers = json.load(f)
    for offer in offers:
        new_offer = Offer(**elem)
        db.session.add(new_offer)
        db.session.commit()

load_offers()



# Представление для получения всех пользователей методом get и post

@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == "GET":
        result = []
        for user in User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == "POST":
        user_data = json.loads(request.data)
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in User.query.all():
            result.append(user.to_dict())

        return jsonify(result), 200

# Представление для получения одного пользователя по id методом get и post, а также удаление методом delete


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(uid):
    if request.method == "GET":
        user = User.query.get(uid)
        return jsonify(user.to_dict()), 200

    if request.method == "PUT":

        user_data = request.json(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = User.query(uid)
        return jsonify(user.to_dict()), 200

    if request.method == "DELETE":
        user = User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "", 204

# Представление для получения всех предложений методом get и post


@app.route('/offers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == "GET":
        result = []
        for offer in Offer.query.all():
            result.append(offer.to_dict())

        return jsonify(result), 200.

    elif request.method == "POST":
        offer_data = json.loads(request.data)
        new_offer = Order(**offer_data)
        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in Offer.query.all():
            result.append(offer.to_dict())


        return jsonify(result), 200

# Представление для получения одного предложения по id методом get и post, а также удаление методом delete

@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(uid):
    if request.method == "GET":
        offer = Offer.query.get(uid)
        return jsonify(offer.to_dict()), 200

    if request_method == "PUT":
        offer_data = request.json(uid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = Offer.query(uid)
        return jsonify(offer.to_dict()), 200

    if request.method == "DELETE":
        offer = User.query.get(uid)
        db.session.delete(offer)
        db.session.commit()

        return "", 204

# Представление для получения всех заказов методом get и post

@app.route('/orders/', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == "GET":
        result = []
        for order in Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200.

    elif request.method == "POST":
        order_data = json.loads(request.data)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in Order.query.all():
            result.append(order.to_dict())

        return jsonify(result), 200

# Представление для получения одного заказа по id методом get и post, а также удаление методом delete

@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(uid):
    if request.method == "GET":
        order = Order.query.get(uid)
        return jsonify(order.to_dict()), 200

    if request_method == "PUT":
        order.id = order_data['id']
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.adress = order_data['adress']
        order.price = order_data['price']
        order.custumer_id = order_data['custumer_id']
        order.executor_id = order_data['executor_id']


        db.session.add(order)
        db.session.commit()

        order = User.query(uid)
        return jsonify(order.to_dict()), 200

    if request.method == "DELETE":
        user = Order.query.get(uid)
        db.session.delete(order)
        db.session.commit()

        return "", 204



if __name__ == '__main__':
    app.run(debug=True, port=1000)