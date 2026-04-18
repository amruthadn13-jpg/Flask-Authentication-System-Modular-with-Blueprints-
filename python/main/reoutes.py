from flask import Blueprint, render_template, session, redirect

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():

    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect("/")


@main.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/")
