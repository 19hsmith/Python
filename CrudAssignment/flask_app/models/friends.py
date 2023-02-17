# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_db').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_db').query_db( query, data )
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM users_db.friends WHERE id = %(id)s"
        return connectToMySQL('users_db').query_db( query, data)
    @classmethod
    def show(cls , data):
        query ='SELECT * FROM users_db.friends WHERE id = %(id)s'
        return connectToMySQL('users_db').query_db( query, data) 
    @classmethod
    def edit(cls , data):
        query ="""UPDATE friends SET first_name = %(fname)s,
            last_name = %(lname)s,
            email = %(email)s,
            updated_at = NOW()
            WHERE id = %(id)s
            """
        return connectToMySQL('users_db').query_db(query, data)