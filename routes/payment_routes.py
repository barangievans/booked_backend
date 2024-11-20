from flask import Blueprint, jsonify, request
import requests
from config import Config  # Import Config

payment_bp = Blueprint('payment', __name__)

# Function to create a payment request to Pesapal
def create_payment_request(order_id, amount, currency="USD", payment_method="mobile_money"):
    headers = {
        "Authorization": f"Bearer {Config.PESAPAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "order_id": order_id,
        "amount": amount,
        "currency": currency,
        "payment_method": payment_method,
        "callback_url": "https://yourwebsite.com/callback",  # Replace with your actual callback URL
    }
    
    response = requests.post(Config.PESAPAL_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the payment link from Pesapal
    else:
        return {"error": "Payment request failed"}

# Define your route for the checkout process
@payment_bp.route('/checkout', methods=['POST'])
def checkout():
    order_data = request.json
    order_id = order_data.get("order_id")
    total_amount = order_data.get("total_amount")
    
    # Create payment request to Pesapal
    payment_response = create_payment_request(order_id, total_amount)
    
    if "error" in payment_response:
        return jsonify(payment_response), 400

    # Return payment link to frontend
    return jsonify({"payment_url": payment_response["payment_url"]})

