from flask_app.config.mysqlconnection import connectToMySQL
class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Dojos"
        results = connectToMySQL('ninjasanddojos').query_db(query)
        dojos = []
        for dojos in results:
            dojos.append( cls(dojos) )
        return dojos
            