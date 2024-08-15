import google.appengine.ext.db as db
from oauth2 import Client
from oauth import OAuth
import time

class MigrationScript:
    def __init__(self):
        self.old_db = db.connect('old_database')
        self.new_db = Client('new_database', auth=OAuth(signature_method_plaintext))

    def fetch_all_data(self):
        return self.old_db.fetch_all()

    def migrate_data(self, data):
        for item in data:
            self.new_db.put(item)

    def run_migration(self):
        start_time = time.time()
        data = self.fetch_all_data()
        self.migrate_data(data)
        end_time = time.time()
        print(f"Migration completed in {end_time - start_time} seconds")

if __name__ == "__main__":
    migration_script = MigrationScript()
    migration_script.run_migration()