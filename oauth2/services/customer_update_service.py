package oauth2.services.customer_update_service

from datetime import datetime, date
from typing import List, Tuple
from sqlalchemy.orm import Session
from models import Customer

class CustomerUpdateService:
    def __init__(self, session: Session):
        self.session = session

    def get_customer_updates(self, last_cutoff: datetime, new_cutoff: datetime) -> List[Customer]:
        end_of_time = datetime(9999, 12, 31, 23, 59, 59, 999999)
        initial_load_date = date(2013, 1, 1)
        customer_changes = []

        try:
            buying_group_changes = self.fetch_buying_group_changes(last_cutoff, new_cutoff)
            for buying_group_change in buying_group_changes:
                customer_data = self.fetch_customer_data(buying_group_change)
                customer_changes.extend(customer_data)

            customer_category_changes = self.fetch_customer_category_changes(last_cutoff, new_cutoff)
            for customer_category_change in customer_category_changes:
                customer_data = self.fetch_customer_data(customer_category_change)
                customer_changes.extend(customer_data)

            self.update_valid_to_dates(customer_changes)

        except Exception as e:
            raise RuntimeError(f'Error retrieving customer updates: {str(e)}')

        return customer_changes

    def fetch_buying_group_changes(self, last_cutoff: datetime, new_cutoff: datetime) -> List[Tuple[int, datetime]]:
        result = self.session.execute(
            "SELECT id, change_date FROM buying_group_changes WHERE change_date BETWEEN :last_cutoff AND :new_cutoff",
            {'last_cutoff': last_cutoff, 'new_cutoff': new_cutoff}
        )
        return result.fetchall()

    def fetch_customer_data(self, change: Tuple[int, datetime]) -> List[Customer]:
        result = self.session.execute(
            "SELECT * FROM customers WHERE buying_group_id = :buying_group_id",
            {'buying_group_id': change[0]}
        )
        return [Customer(**row) for row in result.fetchall()]

    def fetch_customer_category_changes(self, last_cutoff: datetime, new_cutoff: datetime) -> List[Tuple[int, datetime]]:
        result = self.session.execute(
            "SELECT id, change_date FROM customer_category_changes WHERE change_date BETWEEN :last_cutoff AND :new_cutoff",
            {'last_cutoff': last_cutoff, 'new_cutoff': new_cutoff}
        )
        return result.fetchall()

    def update_valid_to_dates(self, customer_changes: List[Customer]):
        for customer in customer_changes:
            future_records = self.session.execute(
                "SELECT MIN(change_date) FROM customer_changes WHERE customer_id = :customer_id AND change_date > :current_date",
                {'customer_id': customer.id, 'current_date': customer.change_date}
            ).scalar()
            customer.valid_to = future_records if future_records else datetime(9999, 12, 31, 23, 59, 59, 999999)