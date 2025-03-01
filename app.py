from flask import Flask, request, jsonify
from flask_cors import CORS
from backend import getSentiments

app = Flask(__name__)
CORS(app)
@app.route("/")
def health():
    return "App is running"

@app.route("/sentiment/<category>")
def sentiment(category):
    return jsonify(getSentiments(category))


if __name__ == '__main__':
    app.run(debug=True)