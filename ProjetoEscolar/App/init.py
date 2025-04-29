# Arquivo __init__.py para tornar a pasta app um pacote Python.
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.crudAlunos import app as alunos_app
    

    app.register_blueprint(alunos_app)
    
    return app 