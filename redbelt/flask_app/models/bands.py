from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask , render_template , redirect , request , flash 
from flask_app import bcrypt
import re 


class Band:
    def __init__(self, data):
        self.id = data['id']
        self.band = data['band'] 
        self.genre = data['genre']
        self.homecity = data['homecity'] 
        self.user_id = data['user_id']
        self.user_info = []

    @classmethod
    def create_band(cls , data):
        query = 'INSERT INTO bands (band, genre, homecity,user_id) VALUES ( %(band)s, %(genre)s, %(homecity)s, %(user_id)s)'
        return connectToMySQL('redbelt_db').query_db(query,data)

    @classmethod
    def delete(cls , data):
        query = "DELETE FROM redbelt_db.bands WHERE id = %(id)s"
        return connectToMySQL('redbelt_db').query_db( query, data)

    @classmethod
    def show_band(cls , data):
        query ='SELECT * FROM redbelt_db.bands WHERE id = %(id)s'
        return connectToMySQL('redbelt_db').query_db( query, data)
         
    @classmethod
    def edit_band(cls , data):
        query ="""UPDATE bands SET band = %(band)s,
                genre = %(genre)s,
                homecity = %(homecity)s
                WHERE id = %(id)s
                """
        return connectToMySQL('redbelt_db').query_db(query, data)

    @classmethod
    def get_band_info(cls):
        query = '''
        SELECT bands.band, bands.genre, bands.homecity,
        users.first_name, users.last_name , bands.id,user_id FROM bands
        JOIN users ON bands.user_id = users.id
        '''
        results = connectToMySQL('redbelt_db').query_db(query)
        print (results)
        if results:
            bands=[]
            for band in results:
                current_band = cls(band)
                current_band.user_info.append(band['first_name'])
                current_band.user_info.append(band['last_name'])
                bands.append(current_band)
            return bands
        else:
            return False
    
    @classmethod
    def get_band_with_user(cls, data):
        query = '''
        SELECT bands.band, bands.genre, bands.homecity,
        users.first_name, users.last_name , bands.id,user_id FROM bands
        JOIN users ON bands.user_id = users.id
        WHERE bands.user_id = %(id)s
        '''
        
        results = connectToMySQL('redbelt_db').query_db(query,data)
        print (results)
        if results:
            bands=[]
            for band in results:
                current_band = cls(band)
                current_band.user_info.append(band['first_name'])
                current_band.user_info.append(band['last_name'])
                bands.append(current_band)
            return bands
        else:
            return False

    @classmethod
    def get_a_band(cls , data):
        query = 'SELECT * FROM bands WHERE id = %(id)s'
        results = connectToMySQL ('redbelt_db').query_db(query,data)
        return results[0]


    @staticmethod
    def validate_music(data):
        is_valid = True

        if len(data['band']) < 2:
            flash('band name must be at least 2 characters long!')
            is_valid = False
        
        if len(data['genre']) < 2:
            flash('genre must be at least 2 characters long!')
            is_valid = False

        return is_valid