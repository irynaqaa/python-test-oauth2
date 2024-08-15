package oauth2.models

from datetime import datetime
from typing import List, Dict
import sqlite3

class Customer:
    def __init__(self, customer_id: int, customer_name: str):
        self.CustomerID = customer_id
        self.CustomerName = customer_name

    @staticmethod
    def fetch_updates(last_cutoff: datetime, new_cutoff: datetime) -> List[Dict]:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Sales.Customers WHERE ValidFrom > ? AND ValidFrom <= ?", (last_cutoff, new_cutoff))
        rows = cursor.fetchall()
        connection.close()
        return [{'CustomerID': row[0], 'CustomerName': row[1]} for row in rows]