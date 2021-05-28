from flask import Flask, render_template,request , redirect , session
import sqlite3

app = Flask(__name__)
app.secret_key = "Sowsy"

@app.route("/")
def top():
    return render_template("base.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect ('/')
        else:
            return render_template("register.html")
    else:
        mail = request.form.get("e-mail")
        name = request.form.get("name")
        password = request.form.get("password")



if __name__ == "__main__":
    app.run(debug=True)