from flask import Flask

from models import db
from data_manager import DataManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

data_manager = DataManager()

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Welcome to MoviWeb!"


@app.route("/users")
def list_users():
    users = data_manager.get_users()
    return str(users)


if __name__ == "__main__":
    app.run(debug=True)
