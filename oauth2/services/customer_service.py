package oauth2.services

from datetime import datetime
from sqlalchemy import create_engine, select, and_, func
from sqlalchemy.orm import sessionmaker
from models import Customer, BuyingGroup, BillToCustomer, CustomerCategory, Person

class CustomerService:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_customer_updates(self, last_cutoff, new_cutoff):
        end_of_time = datetime(9999, 12, 31, 23, 59, 59, 999999)
        customer_changes = []

        session = self.Session()

        buying_group_change_list = session.execute(
            select(BuyingGroup.buying_group_id, BuyingGroup.valid_from)
            .where(and_(BuyingGroup.valid_from > last_cutoff, BuyingGroup.valid_from <= new_cutoff))
        ).fetchall()

        for buying_group_id, valid_from in buying_group_change_list:
            customer_data = session.execute(
                select(Customer.customer_id, Customer.customer_name, BillToCustomer.customer_name, 
                       CustomerCategory.customer_category_name, BuyingGroup.buying_group_name, 
                       Person.full_name, Customer.delivery_postal_code, Customer.valid_from)
                .join(BuyingGroup, BuyingGroup.buying_group_id == Customer.buying_group_id)
                .join(BillToCustomer, BillToCustomer.customer_id == Customer.bill_to_customer_id)
                .join(CustomerCategory, CustomerCategory.customer_category_id == Customer.customer_category_id)
                .join(Person, Person.person_id == Customer.primary_contact_person_id)
                .where(and_(Customer.valid_from <= valid_from, Customer.valid_to >= valid_from))
            ).fetchall()

            for row in customer_data:
                customer_changes.append(dict(row))

        customer_category_change_list = session.execute(
            select(CustomerCategory.customer_category_id, CustomerCategory.valid_from)
            .where(and_(CustomerCategory.valid_from > last_cutoff, CustomerCategory.valid_from <= new_cutoff))
        ).fetchall()

        for customer_category_id, valid_from in customer_category_change_list:
            customer_data = session.execute(
                select(Customer.customer_id, Customer.customer_name, BillToCustomer.customer_name, 
                       CustomerCategory.customer_category_name, BuyingGroup.buying_group_name, 
                       Person.full_name, Customer.delivery_postal_code, Customer.valid_from)
                .join(BuyingGroup, BuyingGroup.buying_group_id == Customer.buying_group_id)
                .join(BillToCustomer, BillToCustomer.customer_id == Customer.bill_to_customer_id)
                .join(CustomerCategory, CustomerCategory.customer_category_id == Customer.customer_category_id)
                .join(Person, Person.person_id == Customer.primary_contact_person_id)
                .where(Customer.valid_from <= valid_from)
            ).fetchall()

            for row in customer_data:
                customer_changes.append(dict(row))

        for change in customer_changes:
            valid_from = change['valid_from']
            valid_to = session.execute(
                select(func.min(Customer.valid_from))
                .where(and_(Customer.customer_id == change['customer_id'], Customer.valid_from > valid_from))
            ).scalar() or end_of_time
            change['valid_to'] = valid_to

        session.close()
        return customer_changes