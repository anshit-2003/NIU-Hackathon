import sqlite3 
from flask import Flask,render_template,request,flash,redirect

app = Flask(__name__)
connection = sqlite3.connect('database.db')
db = connection.cursor()

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/industries")
def login():
    return render_template("Industries.html")

@app.route("/supplier", methods=["GET","POST"])
def supplierlogin():
    if request.method == "GET":
        return render_template("supplier.html")
    else:
        email = request.form.get("email")
        password = request.form.get("pass")
        if email == "ab@gmail.com":
            if password == "ab":
                return redirect("/supplier_dashboard")

@app.route("/supplier_register",methods=["GET","POST"])
def supplierregister():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("pass")
        business = request.form.get("type")
        loc = request.form.get("loc")
        db.execute("INSERT INTO suppliers(username,password,type_of_business,location) VALUES(?,?,?,?)",username,password,business,loc)
        return redirect("/supplier")

@app.route("/industries_register",methods=["GET","POST"])
def industries_register():
    if request.method == "GET":
        return render_template("industries_register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("pass")
        buisness = request.form.get("type")
        location = request.form.get("loc")
        db.execute("INSERT INTO industries(username,password,type_of_buisness,location) VALUES(?,?,?,?)",username, password, buisness,location)
        return redirect("/supplier_dashboard")

@app.route("/supplier_dashboard",methods=["GET","POST"])
def supplier_dash():
    return render_template("supplier_dashboard.html")





if __name__ == '__main__':
    app.run(debug=True)