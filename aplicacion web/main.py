from flask import Flask, jsonify,redirect,url_for,render_template
import requests


app = Flask(__name__)

API_HOST = "http://localhost:8000/user"

@app.route("/")
def home():
    response = requests.get(API_HOST+"/obtener_usuarios")
    return response.json()


if(__name__ == '__main__'):
    app.run(debug=True,port=5000,host='0.0.0.0')