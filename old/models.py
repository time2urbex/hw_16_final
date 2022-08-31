from run import db

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
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    adress = db.Column(db.String(200))
    price = (db.Integer)
    customer_id = db.column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))