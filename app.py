from flask import Flask, render_template, request, redirect, url_for
import os
import requests

from dotenv import load_dotenv

from models import db, Movie
from data_manager import DataManager

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")


def fetch_movie_from_omdb(title, year=None):
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }

    if year:
        params["y"] = year

    response = requests.get("https://www.omdbapi.com/", params=params)
    data = response.json()

    if data.get("Response") == "False":
        return None

    return data


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///moviweb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

data_manager = DataManager()


@app.route("/")
def home():
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    name = request.form.get("name")

    if name:
        data_manager.create_user(name)

    return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["GET", "POST"])
def user_movies(user_id):
    if request.method == "POST":
        name = request.form.get("name")
        year = request.form.get("year")

        if name:
            movie_data = fetch_movie_from_omdb(name, year)

            if movie_data:
                movie = Movie(
                    name=movie_data.get("Title"),
                    director=movie_data.get("Director"),
                    year=int(movie_data.get("Year")),
                    poster_url=movie_data.get("Poster"),
                    user_id=user_id
                )

                data_manager.add_movie(movie)

        return redirect(url_for("user_movies", user_id=user_id))

    movies = data_manager.get_movies(user_id)
    user = data_manager.get_user(user_id)

    return render_template(
        "movies.html",
        movies=movies,
        user=user,
        user_id=user_id
    )


@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    new_name = request.form.get("name")

    if new_name:
        data_manager.update_movie(movie_id, new_name)

    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
