from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = []

# Default Route
@app.route('/')
def hello():
    return jsonify({"Status": "My API server is running"})

# Route for handling GET requests
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data)

# Route for handling POST requests
@app.route('/add_data', methods=['POST'])
def add_data():
    req_data = request.get_json()
    if req_data:
        data.append(req_data)
        return jsonify({"message": "Data added successfully"})
    else:
        return jsonify({"error": "No data provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
