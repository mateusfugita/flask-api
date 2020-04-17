import os
from flask import Flask, request
from flask_cors import CORS
from controllers.essentials import *

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def superheroapi():
    data = request.get_json(force=True)
    apikey = os.getenv("FLASK_APIKEY")
    return searchHero(apikey, data["name"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)