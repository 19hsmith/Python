from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask , render_template , redirect , request , flash 
from flask_app import bcrypt
import re 




EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name']
        self.email = data['email'] 
        self.password = data['password']

    @classmethod 
    def register(cls, data):
        query = 'INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s)' 
        return connectToMySQL ('recipes_db').query_db(query,data)
    
    @classmethod
    def registered(cls):
        query ='SELECT * FROM users;'
        results = connectToMySQL('recipes_db').query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users

    @classmethod
    def log_in(cls, data):
        query ='''
        SELECT email , password 
        FROM users
        WHERE email = %(email)s 
        '''
        results = connectToMySQL('recipes_db').query_db(query,data)
        print('data',data)
        print('results',results)
        if results:
            if data['password'] == results[0]['password']:
                return True
            else: 
                return False
        else:
            return False
        
    @classmethod
    def welcome(cls , data):
        query='SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL ('recipes_db').query_db(query , data)
        return results

    @classmethod
    def get_by_email(cls , data):
        query ='SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL ('recipes_db').query_db(query , data)
        if results and len(results) > 0:
            found_user = cls(results[0])
            return found_user

    @classmethod
    def delete(cls , data):
        query = "DELETE FROM recipes_db.friends WHERE id = %(id)s"
        return connectToMySQL('recipes_db').query_db( query, data)

    @classmethod
    def show(cls , data):
        query ='SELECT * FROM recipes_db.friends WHERE id = %(id)s'
        return connectToMySQL('recipes_db').query_db( query, data) 

    @classmethod
    def edit(cls , data):
        query ="""UPDATE recipe SET  = %(fname)s,
            last_name = %(lname)s,
            email = %(email)s,
            updated_at = NOW()
            WHERE id = %(id)s
            """
        return connectToMySQL('users_db').query_db(query, data)


    @staticmethod
    def validate_new_user(data):
        is_valid = True

        if len(data['first_name']) < 3:
            flash("First Name must be at least 3 characters!", 'register')
            is_valid = False
        
        if len(data['last_name']) < 3:
            flash("Last Name must be at least 3 characters!" , 'register')
            is_valid = False
        
        if not EMAIL_REGEX.match(data['email']):
            flash("email is not valid!" , 'register')
            is_valid = False
        elif User.get_by_email(data):
            flash('Email already registered!' , 'register')
        
        if len(data['password']) < 3:
            flash('password is to short!' , 'register')
            is_valid = False
        
        if data['password'] != data['confirm_password']:
            flash('mismatching password!' , 'register')
            is_valid = False

        return is_valid

    
    @staticmethod
    def validate_log_in(data):
        is_valid = True

        if len(data['email']) == 0:
            flash('Need to fill out email form!' , 'log_in')
            is_valid = False

        if len(data['password']) == 0:
            flash('Need to fill out password form!' , 'log_in')
            is_valid = False    
        return is_valid