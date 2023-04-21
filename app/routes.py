from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name, description, is_planet):
        self.id = id
        self.name = name
        self.description = description
        self.is_planet = is_planet

planets = [
    Planet(1, "Earth", "We live here.", True),
    Planet(2, "Mercury", "The smallest planet.", True),
    Planet(3, "Mars", "Dusty cold desert world.", True),
    Planet(4, "Pluto", "Dwarf planet.", False)
]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({'msg': f"invalid id {planet_id}"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    return abort(make_response({'msg': f"No planet with id {planet_id}"}, 404))

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planets_as_dict = [vars(planet) for planet in planets]
    return jsonify(planets_as_dict), 200

@planets_bp.route("/<planet_id>", methods=['GET'])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id": planet.id,
        "name": planet.name
    }, 200