

class ErrorController:

    def __init__(self, db, os):
        """
        Funcion constructor, se encarga ademas de
        llamar el constructor del padre.
        """
        pass

    def set_type(self, error):
        '''
        Funcion encargada de seleccionar
        el tipo de error que se va a mandar
        '''
        error = int(error)
        return {
            0: 200,
            1: 400,
            2: 401,
            3: 400,
            4: 403,
            5: 500,
            6: 400,
            7: 400,
            8: 504,
            9: 404,
            10: 400,
            11: 426,
            12: 400,
            13: 409
        }.get(error, "404")
