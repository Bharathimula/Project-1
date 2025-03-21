@app.route('/product/search/<keywords>')
def search_product(keyword):
    sample_products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Mouse", "price": 20}
    ]
    result = [p for p in sample_products if keyword.lower() in p["name"].lower()]
    return jsonify(result) if result else jsonify({"message": "No products found"}), 404

