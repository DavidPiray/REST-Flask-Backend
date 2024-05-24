from . import db

class Juego(db.Model):
    __tablename__ = 'juegos'
    id = db.Column(db.String(3), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=True)
    plataforma = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'plataforma': self.plataforma
        }
