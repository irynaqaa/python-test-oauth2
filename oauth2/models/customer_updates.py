package oauth2.models.customer_updates

from typing import Optional
from decimal import Decimal
from datetime import datetime

class Customer:
    def __init__(self, customer_id: int, customer_name: str, bill_to_customer_id: int, customer_category_id: int, buying_group_id: Optional[int], primary_contact_person_id: int, alternate_contact_person_id: Optional[int], delivery_method_id: int, delivery_city_id: int, postal_city_id: int, credit_limit: Optional[Decimal], account_opened_date: datetime, standard_discount_percentage: Decimal, is_statement_sent: bool, is_on_credit_hold: bool, payment_days: int, phone_number: str, fax_number: str, delivery_run: Optional[str], run_position: Optional[str], website_url: str, delivery_address_line1: str, delivery_address_line2: Optional[str], delivery_postal_code: str, delivery_location: Optional[str], postal_address_line1: str, postal_address_line2: Optional[str], postal_postal_code: str, last_edited_by: int, valid_from: datetime, valid_to: datetime):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.bill_to_customer_id = bill_to_customer_id
        self.customer_category_id = customer_category_id
        self.buying_group_id = buying_group_id
        self.primary_contact_person_id = primary_contact_person_id
        self.alternate_contact_person_id = alternate_contact_person_id
        self.delivery_method_id = delivery_method_id
        self.delivery_city_id = delivery_city_id
        self.postal_city_id = postal_city_id
        self.credit_limit = credit_limit
        self.account_opened_date = account_opened_date
        self.standard_discount_percentage = standard_discount_percentage
        self.is_statement_sent = is_statement_sent
        self.is_on_credit_hold = is_on_credit_hold
        self.payment_days = payment_days
        self.phone_number = phone_number
        self.fax_number = fax_number
        self.delivery_run = delivery_run
        self.run_position = run_position
        self.website_url = website_url
        self.delivery_address_line1 = delivery_address_line1
        self.delivery_address_line2 = delivery_address_line2
        self.delivery_postal_code = delivery_postal_code
        self.delivery_location = delivery_location
        self.postal_address_line1 = postal_address_line1
        self.postal_address_line2 = postal_address_line2
        self.postal_postal_code = postal_postal_code
        self.last_edited_by = last_edited_by
        self.valid_from = valid_from
        self.valid_to = valid_to

class BuyingGroup:
    def __init__(self, buying_group_id: int, buying_group_name: str, last_edited_by: int, valid_from: datetime, valid_to: datetime):
        self.buying_group_id = buying_group_id
        self.buying_group_name = buying_group_name
        self.last_edited_by = last_edited_by
        self.valid_from = valid_from
        self.valid_to = valid_to

class CustomerCategory:
    def __init__(self, customer_category_id: int, customer_category_name: str, last_edited_by: int, valid_from: datetime, valid_to: datetime):
        self.customer_category_id = customer_category_id
        self.customer_category_name = customer_category_name
        self.last_edited_by = last_edited_by
        self.valid_from = valid_from
        self.valid_to = valid_to

class Person:
    def __init__(self, person_id: int, full_name: str, preferred_name: str, is_permitted_to_logon: bool, logon_name: Optional[str], is_external_logon_provider: bool, hashed_password: Optional[bytes], is_system_user: bool, is_employee: bool, is_salesperson: bool, phone_number: Optional[str], email_address: Optional[str], last_edited_by: int, valid_from: datetime, valid_to: datetime):
        self.person_id = person_id
        self.full_name = full_name
        self.preferred_name = preferred_name
        self.is_permitted_to_logon = is_permitted_to_logon
        self.logon_name = logon_name
        self.is_external_logon_provider = is_external_logon_provider
        self.hashed_password = hashed_password
        self.is_system_user = is_system_user
        self.is_employee = is_employee
        self.is_salesperson = is_salesperson
        self.phone_number = phone_number
        self.email_address = email_address
        self.last_edited_by = last_edited_by
        self.valid_from = valid_from
        self.valid_to = valid_to