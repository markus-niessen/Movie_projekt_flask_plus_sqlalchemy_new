# 🎬 MovieApp

A web application built with **Flask** and **SQLAlchemy** to manage users and their personal movie collections.

Movie information, including the title, director, release year, and poster, is automatically retrieved from the **OMDb API**.

This project was created as part of the **Masterschool Software Engineering** program.

---

## Features

- Create new users
- Delete users
- View all registered users
- Manage a personal movie collection for each user
- Add movies by title
- Automatically retrieve movie information from the OMDb API
- Display movie posters
- Update movie titles
- Delete movies
- Store all data in a SQLite database
- Custom 404 error page
- Secure API key management using environment variables
- Responsive user interface
- Deployable on PythonAnywhere

---

## Technologies

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- Requests
- python-dotenv
- HTML5
- CSS3
- Jinja2

---

## Project Structure

```text
Movie_projekt_flask_plus_sqlalchemy_new/
│
├── app.py
├── data_manager.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── instance/
│   └── moviweb.db
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── movies.html
│   └── 404.html
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/markus-niessen/Movie_projekt_flask_plus_sqlalchemy_new.git
```

Open the project

```bash
cd Movie_projekt_flask_plus_sqlalchemy_new
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate the virtual environment

```bash
.venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a file named `.env` in the project root.

Example:

```text
OMDB_API_KEY=your_api_key_here
```

You can get a free API key from:

https://www.omdbapi.com/apikey.aspx

---

## Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Database

The application automatically creates the SQLite database on first launch.

Database location:

```text
instance/moviweb.db
```

The database file is ignored by Git and will be created automatically.

---

## Available Routes

| Method | Route | Description |
|---------|-------|-------------|
| GET | / | Show all users |
| POST | /users | Create a new user |
| POST | /users/<user_id>/delete | Delete a user |
| GET | /users/<user_id>/movies | Show a user's movies |
| POST | /users/<user_id>/movies | Add a movie using the OMDb API |
| POST | /users/<user_id>/movies/<movie_id>/update | Update a movie title |
| POST | /users/<user_id>/movies/<movie_id>/delete | Delete a movie |

---

## How It Works

1. Create a user.
2. Open the user's movie collection.
3. Enter a movie title (and optionally a release year).
4. The application requests the movie data from the OMDb API.
5. The movie title, director, year, and poster are automatically saved in the SQLite database.

---

## Screenshots

### Home Page

- View all users
- Add new users
- Delete users

### Movies Page

- Display movie posters
- Add movies
- Update movie titles
- Delete movies

---

## Deployment

The application is ready to be deployed on **PythonAnywhere**.

Live Demo:

https://traumtaenzer82.pythonanywhere.com

---

## Future Improvements

- User authentication
- Search and filter movies
- Movie ratings
- Genres
- Pagination
- Flash messages
- Edit all movie information
- Movie descriptions and runtime

---

## Author

**Markus Nießen**

GitHub:

https://github.com/markus-niessen

---

## License

This project was created for educational purposes as part of the Masterschool Software Engineering curriculum.