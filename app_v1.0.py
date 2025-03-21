
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/products')
def products():
    sample_products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Mouse", "price": 20}
    ]
    return jsonify(sample_products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

