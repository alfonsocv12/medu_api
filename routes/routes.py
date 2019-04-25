import os, sys, bottle
from bottle import route, run, template, response
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from controllers.user_controller import UserController
from controllers.lista_controller import ListaController

application = bottle.default_app()
cred = credentials.Certificate('firestore_env.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
response.content_type = 'application/json'

user_controller = UserController(db)
user_controller.response = response
lista_controller = ListaController(db)
lista_controller.response = response


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

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
