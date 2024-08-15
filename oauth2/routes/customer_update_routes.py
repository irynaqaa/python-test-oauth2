package oauth2.routes

from flask import Blueprint, request, jsonify
from datetime import datetime
from oauth2.services.customer_update_service import CustomerUpdateService

customer_update_routes = Blueprint('customer_update_routes', __name__)

@customer_update_routes.route('/customer_updates', methods=['GET'])
def get_customer_updates():
    last_cutoff = request.args.get('last_cutoff', type=datetime)
    new_cutoff = request.args.get('new_cutoff', type=datetime)
    service = CustomerUpdateService()
    try:
        updates = service.get_customer_updates(last_cutoff, new_cutoff)
        return jsonify([update.to_dict() for update in updates])
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500