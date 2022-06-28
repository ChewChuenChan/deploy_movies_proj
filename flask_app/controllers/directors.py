from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from datetime import datetime
from flask_app.models.director import Director
from flask_app.models.movie import Movie

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/directors')

@app.route('/directors')
def directors():
    directors = Director.get_all()
    return render_template("directors.html", directors=directors)

@app.route('/directors/<int:id>')
def director(id):
    data = {
        'id' : id
    }
    director = Director.get_one(data)
    return render_template("director.html",director = director)

@app.route('/directors/create', methods=["POST"])
def create_director():
    if Director.validate_director(request.form):
        Director.create(request.form)
    return redirect('/directors')

@app.route('/directors/edit/<int:id>')
def edit_director(id):
    data ={
        'id':id
    }
    director = Director.get_one(data)
    return render_template("edit_director.html",director = director )

@app.route('/directors/update/<int:id>', methods=["POST"])
def update_director(id):
    Director.edit(request.form)
    return redirect(f"/directors/{id}")

@app.route('/directors/remove/<int:id>')
def remove_director(id):
    data ={
        'id':id
    }
    director = Director.get_one(data)
    return render_template("delete_director.html",director = director )

@app.route('/directors/delete/<int:id>', methods=["POST"])
def delete_director(id):
    Director.delete (request.form)
    return redirect("/directors")