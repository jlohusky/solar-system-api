import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    # CLOSE THE DATABASE SESSION
    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    # AKA ARRANGE PORTION OF TESTING
    # SET UP A DATABASE
    with app.app_context():
        db.create_all() # RUN ALL THE MIGRATIONS
        yield app

    # CLEAR DATABASE
    with app.app_context():
        db.drop_all()

# CREATE A NEW CLIENT TO SEND OUR REQUESTS
# AKA: creating pytest version of Postman
@pytest.fixture
def client(app):
    return app.test_client()

# POPULATE DATABASE
@pytest.fixture
def two_planets(app):
    planet_one = Planet(id=1, name="Venus", description="Second planet from the sun.", is_planet=True)
    planet_two = Planet(id=2, name="Mercury", description="Smallest planet in our solar system.", is_planet=True)

    db.session.add(planet_one)
    db.session.add(planet_two)
    
    db.session.commit()