from google.appengine.ext import db
import oauth2client
from oauth2client.client import OAuth2WebServerFlow
from apiclient.discovery import build

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

FLOW = OAuth2WebServerFlow(
    client_id='your_client_id',
    client_secret='your_client_secret',
    scope='https://www.googleapis.com/auth/userinfo.email',
    redirect_uri='http://example.com/oauth2callback'
)

SERVICE = build('oauth2', 'v2', http=FLOW.authorize())