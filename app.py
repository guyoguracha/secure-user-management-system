import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, url_for

from forms import RegistrationForm
from models import User, db

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if not app.config["SECRET_KEY"]:
    raise RuntimeError("SECRET_KEY is missing from the .env file.")

db.init_app(app)


@app.get("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        existing_username = db.session.scalar(
            db.select(User).where(User.username == username)
        )
        existing_email = db.session.scalar(
            db.select(User).where(User.email == email)
        )

        if existing_username:
            form.username.errors.append("That username is already registered.")
        elif existing_email:
            form.email.errors.append("That email address is already registered.")
        else:
            user = User(username=username, email=email)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            flash("Your account was created successfully.", "success")
            return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.cli.command("init-db")
def init_db_command():
    db.create_all()
    print("Database tables created successfully.")