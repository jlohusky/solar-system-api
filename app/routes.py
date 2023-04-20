from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, is_planet):
        self.id = id
        self.name = name
        self.description = description
        self.is_planet = is_planet

planets = [
    Planet(1, "Earth", "We live here.", True),
    Planet(2, "Mercury", "The smallest planet.", True),
    Planet(3, "Mars", "Dusty cold desert world.", True)
    Planet(4, "Pluto", "Dwarf planet.", False)
]

