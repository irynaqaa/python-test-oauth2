package oauth2.services

from datetime import datetime
from typing import List, Dict
import pyodbc

def get_customer_updates(last_cutoff: datetime, new_cutoff: datetime) -> List[Dict]:
    end_of_time = datetime(9999, 12, 31, 23, 59, 59, 999999)
    customer_changes = []
    
    connection = pyodbc.connect('your_connection_string')
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE #CustomerChanges (
            CustomerID INT,
            CustomerName VARCHAR(255),
            ValidFrom DATETIME,
            ValidTo DATETIME
        )
    """)
    
    cursor.execute("""
        SELECT BuyingGroupID, ValidFrom 
        FROM BuyingGroups 
        WHERE ValidFrom > ? AND ValidFrom <= ?
    """, (last_cutoff, new_cutoff))
    
    buying_group_change_list = cursor.fetchall()
    
    for buying_group_id, valid_from in buying_group_change_list:
        cursor.execute("""
            SELECT Customer.CustomerID, Customer.CustomerName, ValidFrom 
            FROM Customers 
            JOIN BuyingGroups ON Customers.BuyingGroupID = BuyingGroups.BuyingGroupID 
            WHERE Customers.ValidFrom <= ? AND Customers.ValidTo >= ?
        """, (valid_from, valid_from))
        
        customer_data = cursor.fetchall()
        
        for row in customer_data:
            customer_changes.append({
                'CustomerID': row.CustomerID,
                'CustomerName': row.CustomerName,
                'Valid From': valid_from
            })
    
    cursor.execute("""
        SELECT CustomerCategoryID, ValidFrom 
        FROM CustomerCategories 
        WHERE ValidFrom > ? AND ValidFrom <= ?
    """, (last_cutoff, new_cutoff))
    
    customer_category_change_list = cursor.fetchall()
    
    for customer_category_id, valid_from in customer_category_change_list:
        cursor.execute("""
            SELECT Customer.CustomerID, Customer.CustomerName, ValidFrom 
            FROM Customers 
            JOIN CustomerCategories ON Customers.CustomerCategoryID = CustomerCategories.CustomerCategoryID 
            WHERE Customers.ValidFrom <= ?
        """, (valid_from,))
        
        customer_data = cursor.fetchall()
        
        for row in customer_data:
            customer_changes.append({
                'CustomerID': row.CustomerID,
                'CustomerName': row.CustomerName,
                'Valid From': valid_from
            })
    
    for change in customer_changes:
        valid_from = change['Valid From']
        cursor.execute("""
            SELECT MIN(ValidFrom) 
            FROM Customers 
            WHERE CustomerID = ? AND ValidFrom > ?
        """, (change['CustomerID'], valid_from))
        
        valid_to = cursor.fetchone()[0] or end_of_time
        change['Valid To'] = valid_to
    
    cursor.execute("DROP TABLE #CustomerChanges")
    connection.commit()
    cursor.close()
    connection.close()
    
    return customer_changes