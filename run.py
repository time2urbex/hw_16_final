from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = sqlalchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(debug=True)