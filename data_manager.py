"""Data manager for database CRUD operations."""

from models import Movie, User, db


class DataManager:
    """Handle all database operations for users and movies."""

    def create_user(self, name):
        """Create and save a new user."""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_users(self):
        """Return all users."""
        return User.query.all()

    def get_user(self, user_id):
        """Return a user by ID."""
        return User.query.get(user_id)

    def delete_user(self, user_id):
        """Delete a user and all associated movies."""
        user = User.query.get(user_id)

        if user is None:
            return None

        Movie.query.filter_by(user_id=user_id).delete()

        db.session.delete(user)
        db.session.commit()

        return user

    def get_movies(self, user_id):
        """Return all movies belonging to a user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        """Add a movie to the database."""
        db.session.add(movie)
        db.session.commit()
        return movie

    def update_movie(self, movie_id, new_title):
        """Update the title of a movie."""
        movie = Movie.query.get(movie_id)

        if movie is None:
            return None

        movie.name = new_title
        db.session.commit()
        return movie

    def delete_movie(self, movie_id):
        """Delete a movie by ID."""
        movie = Movie.query.get(movie_id)

        if movie is None:
            return None

        db.session.delete(movie)
        db.session.commit()
        return movie
