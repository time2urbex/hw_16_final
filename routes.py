from models import User
from . import models, db
from flask import current_app as app

# Получаем всех пользователей

@app.route('/users/', methods=['GET', 'POST'])
def users():
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

# Получаем пользователя по id


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(uid):
    if request.method == "GET":
        user = models.User.query.get(uid)
        return jsonify(user.to_dict()), 200

    if request_method == "PUT":
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

# Получаем все офферы


@app.route('/offers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == "GET":
        result = []
        for offer in models.Offer.query.all():
            result.append(order.to_dict())
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

#Получаем офферы по id

@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(uid):
    if request.method == "GET":
        user = models.Offer.query.get(uid)
        return jsonify(offer.to_dict()), 200

    if request_method == "PUT":
        offer_data = request.json(uid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(user)
        db.session.commit()

        offer = models.Offer.query(uid)
        return jsonify(offer.to_dict()), 200

    if request.method == "DELETE":
        user = models.User.query.get(uid)
        db.session.delete(offer)
        db.session.commit()

        return "", 204

#Получаем все заказы

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

#Получаем заказ по uid

@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(uid):
    if request.method == "GET":
        user = models.Order.query.get(uid)
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


        db.session.add(user)
        db.session.commit()

        order = models.User.query(uid)
        return jsonify(order.to_dict()), 200

    if request.method == "DELETE":
        user = models.Order.query.get(uid)
        db.session.delete(order)
        db.session.commit()

        return "", 204


#Добавление пользователя

@app.route('/users/', methods=['POST', 'PUT', 'DELETE'])
def add_user(user):
    max = User(id=3, order_id = 100, last_name='max', executor_id = 32)

    if request.method == "POST":
      data = requests.json
      user = db.session.query(User).get(id)
      user.id = data.get("user")
      user.order_id = data.get("user")
      user.last_name = data.get("user")
      user.executor_id = data.get("user")


    db.session.add(user)
    db.session.commit()

    if request.method == "PUT":
      data = requests.json
      user = db.session.query(User).get(id)
      user.id = data.get("user")
      user.order_id = data.get("user")
      user.last_name = data.get("user")
      user.executor_id = data.get("user")

      db.session.add(user)
      db.session.commit()

    if request.method == "DELETE":
        data = requests.json
        user = db.session.query(User).get(id)
        user.id = data.get("user")
        user.order_id = data.get("user")
        user.last_name = data.get("user")
        user.executor_id = data.get("user")


        db.session.query(user).delete()
        db.session.commit()


#Добавление заказа

@app.route('/orders/', methods=['POST', 'PUT', 'DELETE'])
def add_order(order):

    if request.method == "POST":
      data = requests.json
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

    if request.method == "PUT":
      data = requests.json
      order = db.session.query(Order).get(id)
      order.id = data.get("id")
      order.order_id = data.get("order_id")
      order.last_name = data.get("last_name")
      order.executor_id = data.get("executor_id")

      db.session.add(user)
      db.session.commit()

    if request.method == "DELETE":
        data = requests.json
        order = db.session.query(Order).get(id)
        order.id = data.get("id")
        order.order_id = data.get("order_id")
        order.last_name = data.get("last_name")
        order.executor_id = data.get("executor_id")


        db.session.query(order).delete()
        db.session.commit()


#Добавление оффер

@app.route('/offers/', methods=['POST', 'PUT', 'DELETE'])
def add_offer(order):

    if request.method == "POST":]
      offer_data = request.json(uid)
      offer.order_id = offer_data['order_id']
      offer.executor_id = offer_data['executor_id']

      db.session.add(user)
      db.session.commit()

    db.session.add(order)
    db.session.commit()

    if request.method == "PUT":
      data = requests.json
      offer = db.session.query(Offer).get(id)
      offer.id = data.get("id")
      offer.order_id = data.get("order_id")
      offer.last_name = data.get("last_name")
      offer.executor_id = data.get("executor_id")

      db.session.add(user)
      db.session.commit()

    if request.method == "DELETE":
        data = requests.json
        order = db.session.query(Order).get(id)
        order.id = data.get("order")
        order.order_id = data.get("order")
        order.last_name = data.get("order")
        order.executor_id = data.get("order")


        db.session.query(order).delete()
        db.session.commit()

db.create_all()