from flask import Flask, jsonify, request
app = Flask(__name__)

DATA = [
    {"id":1,"campus":"MMC","lat":25.76,"lon":-80.36},
    {"id":2,"campus":"BBC","lat":25.90,"lon":-80.13},
    {"id":3,"campus":"DC","lat":38.89,"lon":-77.01}

]

next_id = 4

@app.route("/")
def index():
    return"""
    <h1>FIU Campuses API</h1>
    <p> Try these endpoints:</p>
    <ul>
        <li><a href="/api/health">/api/health</a></li>
        <li><a href="/api/data">/api/data</a></li>
        <li><a href="/api/data/1">/api/data/1</a></li>
    </ul>
    """

@app.route("/api/health")
def health():
    return jsonify({"status":"ok"}), 200

@app.route("/api/data")
def items():
    return jsonify(DATA), 200

@app.route("/api/data/<int:id>")
def item(id):
    for i in DATA:
        if i["id"] == id:
            return jsonify(i), 200
    return jsonify({"error":"Item not found"}), 404

@app.route("/api/data", methods=["POST"])
def add_item():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    # Basic validation
    required_fields = ["campus", "lat", "lon"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    new_item = {
        "id": next_id,
        "campus": data["campus"],
        "lat": data["lat"],
        "lon": data["lon"]
    }

    DATA.append(new_item)
    next_id += 1

    return jsonify(new_item), 201

if __name__ =='__main__':
    app.run(debug=True)

