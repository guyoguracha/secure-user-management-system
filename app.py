from flask import Flask, render_template

from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.get("/")
def home():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db_command():
    db.create_all()
    print("Database tables created successfully.")