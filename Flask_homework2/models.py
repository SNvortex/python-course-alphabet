from .db import db

products_transactions = db.Table(
    'products_transactions',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('transaction_id', db.Integer, db.ForeignKey('transaction.id'))
)

products_supermarkets = db.Table(
    'products_supermarkets',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'))
)


class Product(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    price = db.Column(db.Float)
    supermarket_id = db.relationship('Supermarket', secondary=products_supermarkets,
                                     backref=db.backref('supermarket_id'))
    transaction_id = db.relationship('Transaction', secondary=products_transactions,
                                     backref=db.backref('transaction_id'))


class Transaction(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_time = db.Column()
    sum = db.Column(db.Float)


class Supermarket(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    address = db.Column(db.String)
    manager = db.relationship('Manager', backref='supermarket')


class Manager(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    experience = db.Column(db.Integer)
    supermarket = db.Column(db.Integer, db.ForeignKey('supermarket.id'))
