from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

def get_valid_item_by_id(model, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({'msg': f"invalid id {model_id}"}, 400))
    
    item = model.query.get(model_id)
    
    return item if item else abort(make_response({'msg': f"No {model.__name__} with id {model_id}"}, 404))

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    name_query = request.args.get("name")
    is_planet_query = request.args.get("is_planet")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif is_planet_query:
        planets = Planet.query.filter_by(is_planet=is_planet_query)
    else:
        planets = Planet.query.all()

    planet_response = [planet.to_dict() for planet in planets]
    return jsonify(planet_response), 200

@planets_bp.route("/<planet_id>", methods=['GET'])
def handle_planet(planet_id):
    planet = get_valid_item_by_id(Planet, planet_id) 
    return planet.to_dict(), 200

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], is_planet=request_body["is_planet"])

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planets_bp.route("/<planet_id>", methods=['PUT'])
def update_one_planet(planet_id):
    request_body = request.get_json()

    planet_to_update = get_valid_item_by_id(Planet, planet_id)

    planet_to_update.name = request_body["name"]
    planet_to_update.description = request_body["description"]
    planet_to_update.is_planet = request_body["is_planet"]

    db.session.commit()

    return planet_to_update.to_dict(), 200

@planets_bp.route("/<planet_id>", methods=['DELETE'])
def delete_one_planet(planet_id):
    planet_to_delete = get_valid_item_by_id(Planet, planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return f"Planet {planet_to_delete.name} is deleted", 200