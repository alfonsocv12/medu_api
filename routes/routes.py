import os, sys, bottle
from bottle import route, run, template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

application = bottle.default_app()

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@bottle.route('/name/<name>', method='GET')
def sms_post_nucle(name):
    return {'name':name}
