from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__ (self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

    @classmethod
    def get_all_ninja_info(cls):
        query = 'SELECT  FROM ninjas;'
        results = connectToMySQL('ninjasanddojos_db').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas ( Dojos_id , first_name , last_name , age) VALUES ( %(dojo_name)s , %(first_name)s , %(last_name)s , %(age)s );"
        return connectToMySQL ('ninjasanddojos_db').query_db(query, data)
    
    @classmethod
    def show_ninjas(cls,data):
        query = '''
        SELECT ninjas.first_name, ninjas.last_name , ninjas.age , dojos.name
        FROM dojos JOIN ninjas ON dojos.id = ninjas.Dojos_id
        WHERE dojos.id = %(id)s
        '''
        return connectToMySQL ('ninjasanddojos_db').query_db(query, data)

