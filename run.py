from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def superheroapi():
    response = requests.get('https://superheroapi.com/api/1485166761657369/search/batman')
    return response.text

if __name__ == "__main__":
    app.run()