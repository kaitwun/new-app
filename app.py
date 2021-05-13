from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.secret_key = "Sowsy"

@app.route("/")
def top():
    return render_template("base.html")




if __name__ == "__main__":
    app.run(debug=True)