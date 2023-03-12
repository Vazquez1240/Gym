from flask import Flask, jsonify,redirect,url_for,render_template,request
import requests


app = Flask(__name__)

API_HOST = "http://localhost:8000/user"

@app.route("/")
def home():
    data = requests.get(API_HOST+"/obtener_usuarios")
    return data.json()
@app.route("/new_user",methods=["POST","GET"])
def new_user():
    if(request.method == "POST"):
        name = request.form["name"]
        surname = request.form["surname"]
        username = request.form["username"]
        password = request.form["password"]
        number_phone = request.form["number_phone"]
        mail = request.form["mail"]
        user = {"name":name,"surname":surname,"username":username,"password":password,"number_phone":number_phone,
                "mail":mail}
        response = requests.post(API_HOST+'/create_user',json=user)
        if(response.status_code == 201):
            return redirect(url_for('home'))
        else:
            return "error"
    elif(request.method == "GET"):
        print("Entro al get")
        return render_template("login.html")
    else:
        return render_template("login.html")

if(__name__ == '__main__'):
    app.run(debug=True,port=5000,host='0.0.0.0')