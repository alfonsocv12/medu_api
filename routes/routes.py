import os, sys, bottle, json
from bottle import route, run, template, response, error
from error import handler
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from controllers.user_controller import UserController
from controllers.lista_controller import ListaController
try:
    from env import os
    cred = credentials.Certificate(os.environ.get('firebase_json'))
    firebase_admin.initialize_app(cred)
except:
    firestore_cred = os.environ.get('firebase_json')
    firestore_cred = json.loads(firestore_cred)
    cred = credentials.Certificate(firestore_cred)
    firebase_admin.initialize_app(cred)

application = bottle.default_app()
application.error_handle = handler
db = firestore.client()
response.content_type = 'application/json'

user_controller = UserController(db)
user_controller.response = response
lista_controller = ListaController(db)
lista_controller.response = response

@bottle.route('/', method='GET')
def sms_post_nucle():
    return 'hellow happy sunday'

@bottle.route('/name/<name>', method='GET')
def sms_post_nucle(name):
    return {'name':name}

@bottle.route('/all_users', method='GET')
def gel_all_user():
    response.content_type = 'application/json'
    respuesta = user_controller.get_all_users()
    return respuesta

@bottle.route('/one_user', method='GET')
def gel_all_user():
    response.content_type = 'application/json'
    respuesta = user_controller.get_user_logged()
    return respuesta

@bottle.route('/update_user/<user_id>', method='PATCH')
def update_user(user_id):
    response.content_type = 'application/json'
    respuesta = user_controller.update_user(user_id)
    return respuesta

@bottle.route('/lista_salida/<correo_user>', method='PATCH')
def gel_all_user(user_id):
    response.content_type = 'application/json'
    respuesta = user_controller.checar_salida(correo_user)
    return respuesta

@bottle.route('/checar_entrada/<correo_user>', method='POST')
def gel_all_user(correo_user):
    response.content_type = 'application/json'
    respuesta = lista_controller.checar_entrada(correo_user)
    return respuesta

@error(200)
def error200(error):
    error.content_type = 'application/json'
    #db.disconnect('local')
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(404)
def error404(error):
    error.content_type = 'application/json'
    #db.disconnect('local')
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(200)
def error200(error):
    error.content_type = 'application/json'
    #db.disconnect('local')
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(500)
def error500(error):
    error.content_type = 'application/json'
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(400)
def error400(error):
    error.content_type = 'application/json'
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(401)
def error401(error):
    error.content_type = 'application/json'
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta

@error(403)
def error401(error):
    error.content_type = 'application/json'
    body = error.body
    user_controller.errors = lista_controller.errors = []
    respuesta = str({'{}'.format(error.body)})
    return respuesta
