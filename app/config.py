import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://toto:140220@localhost/db_juegos')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
