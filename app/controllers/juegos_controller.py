from flask import Blueprint, request, jsonify
from app.models import Juego
from app import db

# Definir el blueprint para los juegos
juegos_bp = Blueprint('juegos_bp', __name__)

@juegos_bp.route('/game/all', methods=['GET'])
def get_juegos():
    """Obtener todos los juegos de la base de datos"""
    try:
        juegos = Juego.query.all()
        return jsonify([juego.to_dict() for juego in juegos])
    except Exception as e:
        return jsonify({"message": "Ningún juego encontrado en la base de datos","error": str(e)}), 500

@juegos_bp.route('/game/<id>', methods=['GET'])
def get_juego(id):
    """Obtener un juego específico por ID"""
    try:
        juego = Juego.query.get_or_404(id)
        return jsonify(juego.to_dict())
    except Exception as e:
        return jsonify({"message": "Juego no encontrado","error": str(e)}), 500

@juegos_bp.route('/game/add', methods=['POST'])
def add_juego():
    """Agregar un nuevo juego"""
    try:
        data = request.get_json()
        nuevo_juego = Juego(
            id=data['id'],
            nombre=data['nombre'],
            genero=data.get('genero'),
            plataforma=data['plataforma']
        )
        db.session.add(nuevo_juego)
        db.session.commit()
        return jsonify({"message": "Juego agregado exitosamente", "juego": nuevo_juego.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@juegos_bp.route('/game/update/<id>', methods=['PUT'])
def update_juego(id):
    """Actualizar un juego existente"""
    try:
        data = request.get_json()
        juego = Juego.query.get_or_404(id)
        juego.nombre = data['nombre']
        juego.genero = data.get('genero')
        juego.plataforma = data['plataforma']
        db.session.commit()
        return jsonify({"message": "Juego actualizado exitosamente", "juego": juego.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@juegos_bp.route('/game/delete/<id>', methods=['DELETE'])
def delete_juego(id):
    """Eliminar un juego por ID"""
    try:
        juego = Juego.query.get_or_404(id)
        db.session.delete(juego)
        db.session.commit()
        return jsonify({"message": "Juego eliminado exitosamente"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
