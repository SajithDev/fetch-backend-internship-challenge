from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

balance = {} # Dictionary to store the balance of each payer
transactions = [] # List to store each transaction


@app.route('/add', methods=['POST'])
def add_points():
    body = request.get_json()

    # Error validation for payer
    try:
        payer = body['payer']
    except KeyError:
        return 'Error: Payer is required', 400
    
    if len(payer) < 1:   # Check if payer is a valid name
        return 'Error: Payer must be a valid name', 400
    
    # Error validation for points
    try:
        points = body['points']
    except KeyError:
        return 'Error: Points is required', 400
    
    if not (isinstance(points, int)):
        return 'Error: Points must be a valid number', 400

    if points < 0 and balance.get(payer, 0) < abs(points):
        return f'Error: Payer has not added enough points to deduct {abs(points)} points', 400
    
    # Error validation for timestamp
    try:
        timestamp_converted = datetime.strptime(body['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
    except KeyError:
        return 'Error: Timestamp is required and must be in the format: %Y-%m-%dT%H:%M:%SZ', 400


    # Update balance and transactions data for the current transaction
    balance[payer] = (balance.get(payer, 0) + points)
    transactions.append({
            'payer': payer,
            'points': points,
            'timestamp': timestamp_converted
    })

    return '', 200


@app.route('/spend', methods=['POST'])
def spend_points():
    points_removed = {}
    body = request.get_json()

    # Error validation for points to be spent
    try:
        points_spent = body.get('points')
    except KeyError:
        return 'Points to be spent is required', 400

    if points_spent <= 0:
        return 'Points to be spent has to be a positive number', 400
    
    if points_spent > sum(balance.values()):
        return 'User does not have enough points', 400

    # Sort transactions by time (oldest transaction first)
    transactions.sort(key=lambda x: x['timestamp'])

    for transaction in transactions:
        payer = transaction['payer']

        # If points added in a transaction is greater than total points to be spent
        if transaction['points'] >= points_spent:
            points_removed[payer] = points_removed.get(payer, 0) - points_spent
            balance[payer] -= points_spent 
            break   # Points are fully successfully deducted

        else: 
            # All points from specific transaction have been deducted from the payer's balance 
            points_removed[payer] = points_removed.get(payer, 0) - transaction['points']
            balance[payer] -= transaction['points']
            points_spent -= transaction['points']

        if points_spent == 0:
            break   # Points are fully successfully deducted

    return jsonify(points_removed), 200


@app.route('/balance', methods=['GET'])
def get_points_balance():
    return jsonify(balance), 200
    


if __name__ == "__main__":
    app.run(port=8000)
