# -*- coding: utf-8 -*-
from bottle import route, run, redirect, request,HTTPResponse, abort, error
from controllers.error_controller import ErrorController

class BaseController(ErrorController):

    def __init__(self, db):
        '''
        Funcion constructora
        '''
        self.abort = abort
        self.error = error
        self.errors = []
        self.input = {}
        self.db = db

    def error_handle(self, key, message):
        '''
        Funcion encargada de manejar los errores
        '''
        self.errors.append('"mensaje":"{}"'.format(message))
        self.check_errors(key)

    def check_errors(self, error):
        if len(self.errors)>0:
            error = self.set_type(error)
            self.abort(error,", ".join(self.errors))

    def check_if_key(self, dict, key, dafault=None):
        '''
        Funcion dedicada a revisar si el json tiene un valor
        '''
        if key in dict:
            return dict[key]
        return dafault
