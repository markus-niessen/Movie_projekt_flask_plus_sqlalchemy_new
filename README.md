# 🎬 MovieApp (Flask + SQLAlchemy)

A simple web application built with **Flask** and **SQLAlchemy** to manage users and their favorite movies.

This project was created as part of the **Masterschool Software Engineering** program.

---

## Features

- Create new users
- View all registered users
- Manage a personal movie collection for each user
- Add movies
- Update movie titles
- Delete movies
- Store all data in a SQLite database
- Responsive user interface
- Deployable on PythonAnywhere

---

## Technologies

- Python 3
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- Jinja2

---

## Project Structure

```
Movie_projekt_flask_plus_sqlalchemy_new/
│
├── app.py
├── data_manager.py
├── models.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── movies.html
│   └── 404.html
│
└── moviweb.db
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

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Database

The application automatically creates the SQLite database on first launch.

Database file:

```
moviweb.db
```

---

## Available Routes

| Method | Route | Description |
|---------|------|-------------|
| GET | / | Show all users |
| POST | /users | Add a new user |
| GET | /users/<user_id>/movies | Show movies of a user |
| POST | /users/<user_id>/movies | Add a movie |
| POST | /users/<user_id>/movies/<movie_id>/update | Update a movie title |
| POST | /users/<user_id>/movies/<movie_id>/delete | Delete a movie |

---

## Screenshots

### Home Page

- View all users
- Create new users

### Movies Page

- View movies
- Add movies
- Update titles
- Delete movies

---

## Deployment

The application can be deployed on **PythonAnywhere**.

Live Demo:

```
https://traumtaenzer82.pythonanywhere.com
```

---

## Future Improvements

- OMDb API integration
- Automatic movie information lookup
- Movie search
- User authentication
- Movie ratings
- Genres
- Pagination
- Better validation
- Flash messages
- Edit all movie information

---

## Author

**Markus Nießen**

GitHub:

https://github.com/markus-niessen

---

## License

This project is intended for educational purposes as part of the Masterschool Software Engineering curriculum.