import google.appengine.ext.db as db
from oauth2 import Client
from oauth import OAuth
import time

old_db = db.connect('old_database')
new_db = Client('new_database', auth=OAuth(signature_method_plaintext))

data = old_db.fetch_all()

for item in data:
    new_db.put(item)