from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from datetime import datetime
from flask_app.models.director import Director
from flask_app.models.movie import Movie

bcrypt = Bcrypt(app)

@app.route('/movies')
def movies():
    movies = Movie.get_all()
    directors = Director.get_all()
    return render_template("movies.html", movies=movies, directors = directors)

@app.route('/movies/create', methods=["POST"])
def create_movies():
    Movie.create(request.form)
    return redirect('/movies')    