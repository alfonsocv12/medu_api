import json
from datetime import datetime, date
from bottle import request
from controllers.user_controller import UserController
from controllers.base_controller import BaseController

class ListaController(BaseController, UserController):

    def __init__(self, db):
        '''
        Funcion constructora
        '''
        self.db = db
        BaseController.__init__(self, db)

    def checar_entrada(self, correo_user):
        '''
        Funcion encargada de checar_salida
        de los usuarios
        '''
        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        array_entrada, uid = self.get_entrada_array(correo_user, today)
        user_update = self.db.collection('users').document(uid)
        user_update.update({
            'entrada': array_entrada
        })
        return self.get_user_logged(uid)

    def set_entrada(self, array_entrada, today):
        '''
        Funcion encargada
        de marcar la entrada
        '''
        vector_entrada = {}
        vector_entrada['entrada_bolean'] = False
        vector_entrada['fecha_entrada'] = today
        vector_entrada['fecha_salida'] = today
        array_entrada.append(vector_entrada)
        return array_entrada

    def set_salida(self, array_entrada, today):
        '''
        Funcion encargada de
        marcar la salida
        '''
        for entrada in array_entrada:
            if not entrada['entrada_bolean']:
                entrada['entrada_bolean'] = True
                entrada['fecha_salida'] = today
        return array_entrada

    def check_if_entrada(self, user, uid, correo):
        '''
        Funcion encargada de agregar arreglo
        vacio si se requiere
        '''
        try:
            user['entrada']
        except:
            user_update = self.db.collection('users').document(uid)
            user_update.set({
                u'entrada': []
            }, merge=True)
        return self.get_user_logged_correo(correo)

    def get_entrada_array(self, correo, today):
        '''
        Funcion encargada de traer el
        arreglo de entradas
        '''
        abierto = False
        array_entrada = []
        user = self.get_user_logged_correo(correo)
        if not user:
            self.error_handle('06','No existe ese usuario')
        uid = user['uid']
        user = self.check_if_entrada(user, uid, correo)
        if user['entrada']:
            for entrada in user['entrada']:
                if not entrada['entrada_bolean']:
                     abierto = True
                array_entrada.append(entrada)
            if abierto:
                print('entro')
                array_entrada = self.set_salida(array_entrada, today)
            else:
                array_entrada = self.set_entrada(array_entrada, today)
        else:
            array_entrada = self.set_entrada(array_entrada, today)
        return [array_entrada, uid]

    def set_asistencia_intermedia(self, correo_user):
        '''
        Funcion encargada de revisar
        asistencia intermedia
        '''
        user = self.get_user_logged_correo(correo_user)
        uid = self.check_if_key(user, 'uid')
        user_update = self.db.collection('users').document(uid)
        asistencias = self.check_if_key(user, 'asistencias_intermedias')
        valor = self.get_valor_asistensia()
        hoy = str(date.today())
        if not asistencias:
            user_update.set({
                u'asistencias_intermedias':{
                    u'{}'.format(hoy):[
                        valor
                    ]
                }
            }, merge=True)
        else:
            self.add_new_assist(asistencias, user_update, hoy, valor)
        return self.get_user_logged_correo(correo_user)

    def add_new_assist(self, asistencias, user_update, hoy, valor):
        '''
        Funcion encargada de crear una
        nueva asistencia
        '''
        today = self.check_if_key(asistencias, hoy)
        if today:
            today.append(valor)
        else:
            asistencias[hoy]=[valor]
        user_update.set({
            u'asistencias_intermedias': asistencias
        }, merge=True)

    def get_valor_asistensia(self):
        '''
        Funcion encargada de optener
        el valor de la asistencia
        '''
        if request.query.presente:
            return 'Presente'
        return 'Ausente'
