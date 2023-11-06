import requests

def test_star_wars_api():
    response = requests.get("https://swapi.dev/api/planets/")

    # Request should return 200
    assert response.status_code == 200, "API did not return a successful status code."

    # Validate response
    assert response.headers['Content-Type'] == 'application/json', "Content type is not JSON."

    print("The endpoint is up and running!")

# Call the API test function
test_star_wars_api()
