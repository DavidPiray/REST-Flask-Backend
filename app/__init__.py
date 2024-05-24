from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar la base de datos con la aplicación
    db.init_app(app)
    
    # Registrar los blueprints
    from app.controllers.juegos_controller import juegos_bp
    app.register_blueprint(juegos_bp)
    
    return app
