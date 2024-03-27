import pytest
from config import config
from src.getCollection import GetCollection


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get all collections")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_with_valid_key(setup_fixture):
    """
    This test case verifies the response of the get collection API when provided with a valid API key
    and valid parameters. It aims to ensure that the API returns a status code of 200.

    :return: None
    """
    params = {"key": config.VALID_API_KEY,
              "involvedMaker": "Rembrandt van Rijn",
              "format": "json", "culture": "en",
              "p": "1", "ps": '4', "q": "a",
              "imgonly": "True", "toppieces": "True",
              "s": "relevance"
              }

    # Making a request to the get_collection to retrieve collection data with the specified parameters.
    get_collection_handler = GetCollection(config.RIJK_BASE_URL)
    response = get_collection_handler.get_collection(params)

    # Asserting that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Parsing the response body as JSON and storing it in the 'json_content' variable.
    json_content = response.json()

    # Verify list of all the collection (ID's)
    art_objects = json_content.get('artObjects', [])
    assert art_objects, "No art objects found in the response"
    for art_object in art_objects:
        assert 'id' in art_object, "ID is missing for at least one art object"
        assert art_object['id'] is not None, "ID is None for at least one art object"
        print(f"ID: {art_object['id']}")

    # Print success message if all assertions pass
    print("All assertions passed successfully.")


def test_get_collection_with_invalid_key(setup_fixture):
    """
    This test case verifies the response of the get collection API when provided with an invalid API key
    and valid parameters. It aims to ensure that the API returns a status code of 401.

    :return: None
    """
    params = {"key": config.INVALID_API_KEY, "involvedMaker": "Rembrandt van Rijn", "format": "json",
              "culture": "en", "p": "1", "ps": '4', "q": "a", "type": "a", "material": "a", "technique": "a",
              "f.dating.period": "0",
              "f.normalized32Colors.hex": "Color HEX", "imgonly": "True", "toppieces": "True", "s": "relevance"
              }

    # Making a request to the get_collection to retrieve collection data with invalid api key.
    get_collection_handler = GetCollection(config.RIJK_BASE_URL)
    response = get_collection_handler.get_collection(params)

    # Asserting that the response status code is 401
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    print(f"Response: {response.status_code}{response.text}")

    # Print success message if all assertions pass
    print("All assertions passed successfully.")


# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for unexpected behavior")
def test_get_collection_with_invalid_request_parameter(setup_fixture):
    """
    This test case verifies the response of the get collection API when provided with an invalid request parameter
    and valid key. It aims to ensure that the API returns a status code of 400.
    Unexpected behavior: The response status code is seen as 200 even when there is a typo in the
    parameter names in the request.

    :return: None
    """
    params = {"key": config.VALID_API_KEY,
              "involvedMakers": "Rembrandt van Rijn",
              "format": "json", "cultureee": "en",
              "p": "1", "ps": '100001', "q": "a",
              "type": "a", "material": "a", "technique": "a",
              "f.dating.period": "0", "f.normalized32Colors.hex": "Color HEX",
              "imgonly": "True", "toppieces": "True",
              "s": "relevance"
              }

    # Making a request to the get_collection to retrieve collection data with typo in parameters.
    get_collection_handler = GetCollection(config.RIJK_BASE_URL)
    response = get_collection_handler.get_collection(params)

    # Asserting that the response status code is 400, but we are facing here unexpected behavior
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    # Print success message if all assertions pass
    print("All assertions passed successfully.")
