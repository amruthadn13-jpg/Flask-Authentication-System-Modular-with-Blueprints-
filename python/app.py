from flask import Flask
from auth.routes import auth
from main.routes import main

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(auth)
app.register_blueprint(main)

app.run(debug=True)
