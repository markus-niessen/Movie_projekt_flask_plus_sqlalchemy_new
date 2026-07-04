from flask import Flask, render_template, request, redirect, url_for
from models import db
from data_manager import DataManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///moviweb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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
        director = request.form.get("director")
        year = request.form.get("year")
        poster_url = request.form.get("poster_url")

        if name and director and year and poster_url:
            data_manager.add_movie(
                user_id=user_id,
                name=name,
                director=director,
                year=int(year),
                poster_url=poster_url
            )

        return redirect(url_for("user_movies", user_id=user_id))

    movies = data_manager.get_movies(user_id)
    return render_template("movies.html", movies=movies, user_id=user_id)


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


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
