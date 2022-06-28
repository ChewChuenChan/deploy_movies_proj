from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from flask import flash
from flask_bcrypt import Bcrypt
import re
from flask_app.models import director


class Movie:

    db = "movies_db"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        self.director_id = data['director_id']
        self.director = None
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies JOIN directors ON directors.id = movies.director_id;"
        result = connectToMySQL(cls.db).query_db(query)
        movies_list =[]
        for row in result:
            #create the movie object
            movie_ob = cls(row)
            #create the director object
            director_data ={
                'id':row['directors.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name']
            }
            director_ob = director.Director(director_data)
            #associate the two objects together
            movie_ob.director = director_ob
            movies_list.append(movie_ob)
        return movies_list

    @classmethod
    def create(cls,data):
        query = "INSERT INTO movies (title, release_date,director_id ) VALUES (%(title)s, %(release_date)s, %(director_id)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result