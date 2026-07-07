"""Flask application for managing users and their favorite movies."""

import os

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from data_manager import DataManager
from models import Movie, db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
OMDB_API_URL = "https://www.omdbapi.com/"


def fetch_movie_from_omdb(title, year=None):
    """Fetch movie data from the OMDb API by title and optional year."""
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }

    if year:
        params["y"] = year

    try:
        response = requests.get(OMDB_API_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()

    if data.get("Response") == "False":
        return None

    return data


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///moviweb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create database tables if they do not already exist.
with app.app_context():
    db.create_all()

data_manager = DataManager()


@app.route("/")
def home():
    """Display all users."""
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    """Add a new user."""
    name = request.form.get("name")

    if name:
        data_manager.create_user(name)

    return redirect(url_for("home"))


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete a user by ID."""
    data_manager.delete_user(user_id)
    return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["GET", "POST"])
def user_movies(user_id):
    """Display and add movies for a specific user."""
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
    """Update the title of a movie."""
    new_name = request.form.get("name")

    if new_name:
        data_manager.update_movie(movie_id, new_name)

    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete a movie by ID."""
    data_manager.delete_movie(movie_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.errorhandler(404)
def page_not_found(error):
    """Display a custom 404 error page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
    