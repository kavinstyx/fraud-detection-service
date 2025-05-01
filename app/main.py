from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Create a simple anomaly detection model
model = IsolationForest(contamination=0.05)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Fraud Detection API is running"})

@app.route('/api/detect', methods=['POST'])
def detect_fraud():
    data = request.json
    
    # Extract features from procurement data
    features = np.array([[
        data.get('amount', 0),
        data.get('supplier_history', 0),
        data.get('time_to_delivery', 0),
        data.get('price_variance', 0)
    ]])
    
    # Dummy prediction for now
    prediction = -1 if np.random.random() < 0.1 else 1
    
    return jsonify({
        'transaction_id': data.get('transaction_id'),
        'is_fraudulent': prediction == -1,
        'confidence': float(0.85)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)