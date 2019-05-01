import json
from datetime import datetime
from controllers.user_controller import UserController

class ListaController(UserController):

    def __init__(self, db):
        '''
        Funcion constructora
        '''
        self.db = db

    def checar_entrada(self, correo_user):
        '''
        Funcion encargada de checar_salida
        de los usuarios
        '''
        array_entrada, uid = self.get_entrada_array(correo_user)
        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_update = self.db.collection('users').document(uid)
        vector_entrada = {}
        vector_entrada['entrada_bolean'] = False
        vector_entrada['fecha_entrada'] = str(datetime)
        vector_entrada['fecha_salida'] = str(datetime)
        array_entrada.append(vector_entrada)
        user_update.update({
            'entrada': array_entrada
        })
        return self.get_user_logged(uid)

    def get_entrada_array(self, correo):
        '''
        Funcion encargada de traer el
        arreglo de entradas
        '''
        array_entrada = []
        user = self.get_user_logged_correo(correo)
        uid = user['uid']
        if user['entrada']:
            for entrada in user['entrada']:
                if not entrada['entrada_bolean']:
                     return ['','']
                array_entrada.append(entrada)
            return [array_entrada, uid]
        return [array_entrada, uid]
