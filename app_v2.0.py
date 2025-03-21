
from flask import request

@app.route('/products/search')
def search_product_query():
    keyword = request.args.get("q", "")
    if not keyword:
        return jsonify({"error": "Missing search query"}), 400
    
    sample_products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Mouse", "price": 20}
    ]
    result = [p for p in sample_products if keyword.lower() in p["name"].lower()]
    
    return jsonify(result) if result else jsonify({"message": "No products found"}), 404

