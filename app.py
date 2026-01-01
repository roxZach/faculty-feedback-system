from flask import Flask,render_template
from config import cursor

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test-db")
def test_db():
    cursor.execute("SHOW TABLES")
    return "Database Connected"

if(__name__=="__main__"):
    app.run(debug=True)