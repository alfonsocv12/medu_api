import json
from bottle import request

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

    def get_user_logged(self, user_id=None):
        '''
        Funcion encargada de traer un user
        por su id
        '''
        if not user_id:
            user_id = request.forms.getone('user_id', None)
        doc_ref = self.db.collection('users')
        users = doc_ref.where('uid','==',user_id).stream()
        vector_user = {}
        for user in users:
            vector_user = user.to_dict()
        return json.dumps(vector_user, indent=4, sort_keys=True)

    def update_user(self, user_id):
        '''
        Funcion encargada de hacer un
        '''
        apellido = request.forms.getone('apellido', None)
        user_update = self.db.collection('users').document(user_id)
        vector_user = {}
        vector_user['apellido'] = apellido
        user_update.update(vector_user)
        return self.get_user_logged(user_id)
