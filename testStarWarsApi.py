import requests

def test_star_wars_api():
    response = requests.get("https://swapi.dev/api/planets/")

    # Verify response is 200
    assert response.status_code == 200, "API did not return a successful status code."

    # Verify header
    assert response.headers['Content-Type'] == 'application/json', "Not JSON."

    # Verify JSON structure
    data = response.json()
    assert isinstance(data, dict), "Response not JSON"

    # Check JSON keys
    expected_keys = {'count', 'next', 'previous', 'results'}
    assert expected_keys.issubset(data.keys()), "Not expected keys"

    print("The endpoint is UP AND RUNNING and all tests PASSED")

'''Run Tests'''
test_star_wars_api()
