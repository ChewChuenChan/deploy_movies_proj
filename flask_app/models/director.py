from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from flask import flash
from flask_bcrypt import Bcrypt
import re
from flask_app.models import movie


bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Director:
    db = "movies_db"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM directors;"
        result = connectToMySQL(cls.db).query_db(query)
        director_list =[]
        for row in result:
            director_list.append(cls(row))
        return director_list

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM directors WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        this_director = cls(result[0])
        return this_director

    @classmethod
    def create(cls,data):
        query = "INSERT INTO directors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def edit(cls,data):
        query = "UPDATE directors SET first_name = %(first_name)s, last_name=%(last_name)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM directors WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @staticmethod
    def validate_director(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.","register")
        if len(user_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.","register")
            is_valid = False
        return is_valid
