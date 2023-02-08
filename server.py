from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo à minha API!"

@app.route("/dados")
def dados():
    return jsonify({"dados": [1, 2, 3, 4]})



if __name__ == "__main__":
    app.run(debug=True)