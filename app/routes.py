from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({'msg': f"invalid id {planet_id}"}, 400))
    
    all_planets = Planet.query.all()

    for planet in all_planets:
        if planet.id == planet_id:
            return planet
    
    return abort(make_response({'msg': f"No planet with id {planet_id}"}, 404))

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    all_planets = Planet.query.all()

    planet_response = []
    for planet in all_planets:
        planet_response.append(planet.to_dict())
    return jsonify(planet_response), 200

@planets_bp.route("/<planet_id>", methods=['GET'])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "is_planet": planet.is_planet
    }, 200

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], is_planet=request_body["is_planet"])

    db.session.add(new_planet)
    db.session.commit()

    return {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "is_planet": new_planet.is_planet
    }, 201