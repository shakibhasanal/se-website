from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    # Add authentication logic here
    return f"Logged in as {email}"

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    # Add registration logic here
    return f"Registered successfully with username: {username}"

if __name__ == "__main__":
    app.run(debug=True)
