package oauth2.controllers

from datetime import datetime
from typing import List, Dict
from oauth2.services.customer_updates_service import CustomerUpdatesService

class CustomerUpdatesController:
    def retrieve_customer_updates(self, last_cutoff: datetime, new_cutoff: datetime) -> List[Dict]:
        if not isinstance(last_cutoff, datetime) or not isinstance(new_cutoff, datetime):
            raise ValueError("Both last_cutoff and new_cutoff must be datetime objects")
        customer_updates = CustomerUpdatesService.get_customer_updates(last_cutoff, new_cutoff)
        return customer_updates