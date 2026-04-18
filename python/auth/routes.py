from flask import Blueprint, request, redirect, render_template, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db

auth = Blueprint("auth", __name__)

# REGISTER
@auth.route("/register", methods=["POST"])
def register():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        flash(" Username already exists", "error")

    else:
        hashed = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        flash(" Registered Successfully", "success")

    conn.close()
    return redirect("/")


# LOGIN
@auth.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user and check_password_hash(user[2], password):
        session["user"] = username
        flash(" Login Successful", "success")
        return redirect("/dashboard")

    else:
        flash(" Invalid Credentials", "error")
        return redirect("/")
