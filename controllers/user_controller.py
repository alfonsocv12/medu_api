import json

class UserController():

    def __init__(self, db):
        '''
        Funcion constructora
        '''
        self.db = db

    def get_all_users(self):
        '''
        Funcion encargada de traer todos los usuarios
        '''
        array_users = []
        doc_ref = self.db.collection('users').stream()
        for doc in doc_ref:
            vector = {}
            vector['id'] = doc.id
            vector = doc.to_dict()
            array_users.append(vector)
        return json.dumps(array_users, indent=4, sort_keys=True)
