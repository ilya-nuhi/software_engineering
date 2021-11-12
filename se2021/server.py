from flask import Flask, jsonify

app = Flask(__name__)

def encode(phrase):
    return "...---..."

@app.route("/")
def hello():
    payload = {"message":"Hello, world"}
    return jsonify(payload)
@app.route("/morse/<phrase>")
def morse(phrase):
    payload = {"result": encode(phrase)}
    return jsonify(payload)

if __name__ == "__main__":
    app.run()