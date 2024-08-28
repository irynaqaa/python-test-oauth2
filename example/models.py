from google.appengine.ext import db

class User(db.Model):
  username = db.StringProperty(required=True)
  email = db.EmailProperty()
  created_at = db.DateTimeProperty(auto_now_add=True)

class Product(db.Model):
  name = db.StringProperty(required=True)
  description = db.TextProperty()
  price = db.FloatProperty(required=True)
  created_at = db.DateTimeProperty(auto_now_add=True)

class Order(db.Model):
  user = db.ReferenceProperty(User, required=True)
  product = db.ReferenceProperty(Product, required=True)
  quantity = db.IntegerProperty(required=True)
  total_price = db.FloatProperty(required=True)
  created_at = db.DateTimeProperty(auto_now_add=True)