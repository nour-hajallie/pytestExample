import pytest

from config import config
from src.get_collection import GetCollection
from src.responseHandler import ResponseHandler


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get all collections")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_with_valid_key(setup_fixture):
    '''
    The objective of this test is to check response of get collection API
    with a valid key and valid parameters
    :return: None
    '''
    params = {"key": config.VALID_API_KEY,
              "involvedMaker": "Rembrandt van Rijn",
              "format": "json", "culture": "en",
              "p": "1", "ps": '4', "q": "a",
              "imgonly": "True", "toppieces": "True",
              "s": "relevance"
              }
    getCollectionHandler = GetCollection(config.BASE_URL)
    response = getCollectionHandler.get_collection(params)
    ResponseHandler.assert_successful_response(response)
    json_content = response.json()
    # Verify list of all the collection (ID's)
    id_values = [art_object['id'] for art_object in json_content.get('artObjects', [])]
    print(id_values)
    assert all(id_value is not None for id_value in id_values), "At least one 'id' value is None"

def test_get_collection_with_invalid_key(setup_fixture):
    '''
    The objective of this test is to check response of get collection API
    with an invalid key and valid parameters
    :return: None
    '''
    params = {"key": config.INVALID_API_KEY, "involvedMaker": "Rembrandt van Rijn", "format": "json"
        , "culture": "en",
              "p": "1", "ps": '4', "q": "a", "type": "a", "material": "a", "technique": "a", "f.dating.period": "0",
              "f.normalized32Colors.hex": "Color HEX", "imgonly": "True", "toppieces": "True", "s": "relevance"
              }
    getCollectionHandler = GetCollection(config.BASE_URL)
    response = getCollectionHandler.get_collection(params)
    ResponseHandler.assert_unauthorised_response(response)

# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_get_collection_with_invalid_request_parameter(setup_fixture):
    '''
    The objective of this test is to check response of get collection API
    with a wrong parameter and valid key
    the wrong parameter passed is "psrr" instead of "ps", "mat" instead of "material"
    :return: None
    '''
    params = {"key": config.VALID_API_KEY,
              "involvedMaker": "Rembrandt van Rijn",
              "format": "json", "culture": "en",
              "p": "1", "psrr": '100001', "q": "a",
              "type": "a", "mat": "a", "technique": "a",
              "f.dating.period": "0","f.normalized32Colors.hex": "Color HEX",
              "imgonly": "True", "toppieces": "True",
              "s": "relevance"
              }
    getCollectionHandler = GetCollection(config.BASE_URL)
    response = getCollectionHandler.get_collection(params)
    ResponseHandler.assert_unsuccessful_response_invalid_parameter(response)
