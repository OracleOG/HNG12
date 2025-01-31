from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def get_info():
    return jsonify({
        "email": "emmanuelnwafor212@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/OracleOG/HNG12/"
    })

if __name__ == "__main__":
    app.run(debug=True)

