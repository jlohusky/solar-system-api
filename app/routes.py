from flask import Blueprint, jsonify

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

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planets_as_dict = [vars(planet) for planet in planets]
    return jsonify(planets_as_dict), 200