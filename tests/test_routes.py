def test_get_all_planets_with_empty_db_returns_empty_list(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_all_planets_with_populated_db(client, two_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == [
        {
            "id": 1,
            "name": "Venus",
            "description": "Second planet from the sun.",
            "is_planet": True
        },
        {
            "id": 2,
            "name": "Mercury",
            "description": "Smallest planet in our solar system.",
            "is_planet": True
        }
    ]
    assert response.status_code == 200

def test_get_one_planet_returns_one_planet(client, two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["name"] == "Venus"
    assert response_body["description"] == "Second planet from the sun."
    assert response_body["is_planet"] == True

def test_returns_404_with_missing_planet_id(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_post_one_planet_create_planet_in_db(client):
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "Poor Pluto!",
        "is_planet": False
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["name"] == "Pluto"
    assert response_body["description"] == "Poor Pluto!"
    assert response_body["is_planet"] == False