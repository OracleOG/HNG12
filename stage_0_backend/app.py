from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def get_info():
    return jsonify({
        "email": "your-email@example.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/yourusername/your-repo"
    })

if __name__ == "__main__":
    app.run(debug=True)

