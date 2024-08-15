from google.appengine.ext import db
from google.appengine.api import users

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)

class Product(db.Model):
    name = db.StringProperty(required=True)
    description = db.TextProperty()
    price = db.FloatProperty(required=True)

class Order(db.Model):
    user = db.ReferenceProperty(User, required=True)
    product = db.ReferenceProperty(Product, required=True)
    order_date = db.DateTimeProperty(auto_now_add=True)