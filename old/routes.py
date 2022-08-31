from run import db
import models
from flask import current_app as app
import json
from flask import jsonify


# Представление для получения всех пользователей методом get и post

@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == "GET":
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == "POST":
        user_data = json.loads(request.data)
        print(user_data)
        new_user = models.User(**user_data)
        print(new_user.to_dict())
        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())

        return jsonify(result), 200

# Представление для получения одного пользователя по id методом get и post, а также удаление методом delete


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(uid):
    if request.method == "GET":
        user = models.User.query.get(uid)
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

        user = models.User.query(uid)
        return jsonify(user.to_dict()), 200

    if request.method == "DELETE":
        user = models.User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "", 204

# Представление для получения всех предложений методом get и post


@app.route('/offers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == "GET":
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())

        return jsonify(result), 200.

    elif request.method == "POST":
        offer_data = json.loads(request.data)
        new_offer = models.Order(**offer_data)
        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())


        return jsonify(result), 200

# Представление для получения одного предложения по id методом get и post, а также удаление методом delete

@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(uid):
    if request.method == "GET":
        offer = models.Offer.query.get(uid)
        return jsonify(offer.to_dict()), 200

    if request_method == "PUT":
        offer_data = request.json(uid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = models.Offer.query(uid)
        return jsonify(offer.to_dict()), 200

    if request.method == "DELETE":
        offer = models.User.query.get(uid)
        db.session.delete(offer)
        db.session.commit()

        return "", 204

# Представление для получения всех заказов методом get и post

@app.route('/orders/', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == "GET":
        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200.

    elif request.method == "POST":
        order_data = json.loads(request.data)
        new_order = models.Order(**order_data)
        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())

        return jsonify(result), 200

# Представление для получения одного заказа по id методом get и post, а также удаление методом delete

@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(uid):
    if request.method == "GET":
        order = models.Order.query.get(uid)
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

        order = models.User.query(uid)
        return jsonify(order.to_dict()), 200

    if request.method == "DELETE":
        user = models.Order.query.get(uid)
        db.session.delete(order)
        db.session.commit()

        return "", 204

db.create_all()
