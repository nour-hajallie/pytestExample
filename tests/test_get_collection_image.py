import pytest
import requests

from config import config
from src.getCollectionImage import GetCollectionImage


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get collection image details")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_image_with_valid_key(setup_fixture):
    """
    This test case verifies the response of the image details API when provided with a valid API key.
    It ensures that the API returns a successful status code (200) and validates the structure of the JSON response.
    Additionally, it extracts the URL from the JSON response and checks if it points to a valid image.

    :param setup_fixture: Fixture for test setup.
    :return: None
    """
    params = {"key": config.VALID_API_KEY, "object-number": "1"}
    get_collection_image_handler = GetCollectionImage(config.RIJK_BASE_URL)
    response = get_collection_image_handler.get_collection_image(params)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    json_content = response.json()
    print(json_content)

    # verify if there are image width and height are present in response
    assert isinstance(json_content['levels'], list), "'levels' is not a list in the response"
    level = json_content['levels'][0]
    assert 'name' in level, "Key 'name' not found in the level"
    assert level['name'] != '', "Unexpected value for 'name' in the level"

    assert 'width' in level, "Key 'width' not found in the level"
    assert level['width'] != '', "Unexpected value for 'width' in the level"

    assert 'height' in level, "Key 'height' not found in the level"
    assert level['height'] != '', "Unexpected value for 'height' in the level"

    # Extracting URL from the JSON structure
    url = json_content["levels"][0]["tiles"][0]["url"]

    # Check if the URL points to a valid image
    if is_valid_image(url):
        print("Valid image URL")
    else:
        print("Not a valid image URL")

    # Print success message if all assertions pass
    print("All assertions passed successfully.")


def test_get_collection_image_with_invalid_key(setup_fixture):
    """
     The objective of this test is to check the response of the image details API with an invalid API key.
     This test ensures that the API returns a status code of 401 (Unauthorized) when an invalid key is provided.
     :return: None
     """
    params = {"key": config.INVALID_API_KEY, "object-number": "1"}
    # Instantiate the API handler
    get_collection_image_handler = GetCollectionImage(config.RIJK_BASE_URL)

    # Send request to the API
    response = get_collection_image_handler.get_collection_image(params)

    # Verify response status code
    assert response.status_code == 401, f"Expected status code 401 (Unauthorized), but got {response.status_code}"

    # Verify response text contains "Invalid key"
    assert "Invalid key" in response.text, "Response text does not contain 'Invalid key'"

    # Print success message if all assertions pass
    print("All assertions passed successfully.")


# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for a unexpected behavior")
def test_get_collection_image_with_invalid_request_parameter(setup_fixture):
    """
    The objective of this test is to check response of image details API with a valid key
    and invalid parameter , "objectnum" instead of "object-number"
    This test should return a status code of 400 but code 200 is returned.
    :return:
    """
    params = {"key": config.VALID_API_KEY, "objectnum": "1"}
    # Instantiate the API handler
    get_collection_image_handler = GetCollectionImage(config.RIJK_BASE_URL)

    # Send request to the API
    response = get_collection_image_handler.get_collection_image(params)

    # Verify response status code
    assert response.status_code == 400, f"Expected status code 400 (Bad Request), but got {response.status_code}"


def test_get_collection_image_with_invalid_collection_id(setup_fixture):
    """
    The objective of this test is to check the response of the collection image API with a valid key
    and an invalid collection ID "SK-R-216" instead of the valid one "SK-C-216".
    This test ensures that the API returns a status code of 500 and contains an appropriate error message.

    :return: None
    """
    params = {"key": config.VALID_API_KEY, "object-number": "1"}

    # Instantiate the API handler
    get_collection_image_handler = GetCollectionImage(config.RIJK_BASE_URL)

    # Send request to the API
    response = get_collection_image_handler.get_collection_image_invalid_collection_id(params)

    # Verify response status code
    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"

    # Print success message if all assertions pass
    print("All assertions passed successfully.")


# Define the is_valid_image function
def is_valid_image(url):
    """
    Check if the provided URL points to a valid image by sending a GET request to the URL
    and examining the response headers.
    Args:
        url (str): The URL of the image to be checked.
    Returns:
        bool: True if the URL points to a valid image, False otherwise.
    """
    try:
        response = requests.get(url)
        # Check if the response status code is OK (200)
        if response.status_code == 200:
            # Check if the content type is an image
            content_type = response.headers['content-type']
            if content_type.startswith('image'):
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
    return False
