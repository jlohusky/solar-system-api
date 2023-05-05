from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    is_planet = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_planet": self.is_planet
        }
    
    @classmethod
    def from_dict(cls, planet_details):
        new_planet = cls(
            name=planet_details["name"],
            description=planet_details["description"],
            is_planet=planet_details["is_planet"]
        )
        return new_planet