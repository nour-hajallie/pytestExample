import pytest

from config import config
from src.getCollectionDetails import GetCollectionDetails


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get all collections")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_details_with_valid_key(setup_fixture):
    '''
    This test case verifies the response of the collection details API when provided with a valid API key.
    It ensures that the API returns a successful status code (200) and validates the structure of the JSON response.
    Additionally, it checks if the expected keys ('artObject' and 'artObjectPage') are present in the response.
    It also verifies if the object numbers in 'artObject' match the expected value from the configuration.

    :return: None
    '''
    params = {"key": config.VALID_API_KEY,
              "format": "json", "culture": "en",
              "object-number": "1"
              }
    get_collection_details_handler = GetCollectionDetails(config.RIJK_BASE_URL)
    response = get_collection_details_handler.get_collection_details(params)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    json_content = response.json()
    print(json_content)

    # Verify if the art object and art object page  about the selected collection is found
    assert 'artObject' in json_content, "Expected key 'artObject' not found in response"
    assert 'artObjectPage' in json_content, "Expected key 'artObjectPage' not found in response"

    # Verify if the object numbers in artObject match the expected value from the config
    expected_object_numbers = config.VALID_COLLECTION_ID
    actual_object_numbers = json_content.get('artObject',{}).get('classification', {}).get('objectNumbers', [])

    # Convert the actual object numbers list to a string
    actual_object_numbers_str = ', '.join(actual_object_numbers)
    assert actual_object_numbers_str == expected_object_numbers, f"Expected object numbers {expected_object_numbers}, but got {actual_object_numbers_str}"
    # Print success message if all assertions pass
    print("All assertions passed successfully.")
def test_get_collection_details_with_invalid_collection_id(setup_fixture):
    '''
    This test case verifies the response of the collection details API when provided with a valid API key
    and an invalid collection ID ("SK-R-216" instead of the valid one "SK-C-216").
    It ensures that the API returns an error status code (500) due to the invalid collection ID.

    :return: None
    '''
    params = {"key": config.VALID_API_KEY, "format": "json", "culture": "en",
              "object-number": "1"}
    get_collection_details_handler = GetCollectionDetails(config.RIJK_BASE_URL)
    # Send request to the API
    response = get_collection_details_handler.get_collection_details_invalid_collection_id(params)

    # Verify response status code
    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"

    # Print response status code and text for investigation
    print(f"Response: {response.status_code}{response.text}")

    # Print success message if all assertions pass
    print("All assertions passed successfully.")

# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for unexpected behavior")
def test_get_collection_details_with_invalid_request_parameter(setup_fixture):
    '''
    This test case verifies the response of the collection details API when provided with a valid API key
    and an incorrect parameter ('for' instead of 'format').
    It ensures that the API returns a status code of 400 due to the invalid request parameter.
    unexpected behaviour: the response is seen 200 even there is a typo with parameter names in the request

    :return:
    '''
    params = {"key": config.VALID_API_KEY, "for": "html", "culture": "en",
              "object-number": "1"}
    get_collection_details_handler = GetCollectionDetails(config.RIJK_BASE_URL)
    # Send request to the API
    response = get_collection_details_handler.get_collection_details(params)

    # Verify response status code
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    # Print success message if all assertions pass
    print("All assertions passed successfully.")
def test_get_collection_details_with_invalid_parameter_value(setup_fixture):
    '''
     This test case verifies the response of the collection details API when provided with a valid API key
    and an incorrect parameter value ('htmls' instead of 'html' for the format).
    It ensures that the API returns a status code of 404 due to the invalid parameter value.

    :return:
    '''
    params = {"key": config.VALID_API_KEY, "format": "htmls", "culture": "en",
              "object-number": "1"}
    get_collection_details_handler = GetCollectionDetails(config.RIJK_BASE_URL)
    # Send request to the API
    response = get_collection_details_handler.get_collection_details(params)

    # Verify response status code
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

    # Print response status code and text for further investigation
    print(f"Response: {response.status_code}{response.text}")

    # Print success message if all assertions pass
    print("All assertions passed successfully.")
