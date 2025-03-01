from flask import Flask, request
from backend import getSentiments

app = Flask(__name__)

@app.route("/")
def health():
    return "App is running"

@app.route("/sentiment")
def sentiment():
    return getSentiments()

if __name__ == '__main__':
    app.run(debug=True)