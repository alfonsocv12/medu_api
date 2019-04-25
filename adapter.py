from bottle import run
from routes.routes import bottle
from routes.routes import application

if __name__ == "__main__":
    run(host='localhost', port=85, debug=True)
