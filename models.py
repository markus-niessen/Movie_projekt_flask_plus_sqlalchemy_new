"""Database models for the Movie application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Database model representing an application user."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Movie(db.Model):
    """Database model representing a user's favorite movie."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(255), nullable=False)

    # Foreign key linking the movie to its owner.
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
