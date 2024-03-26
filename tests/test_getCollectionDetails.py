import pytest

from config import config
from src.get_collection_details import GetCollectionDetails
from src.responseHandler import ResponseHandler


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get all collections")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_details_with_valid_key(setup_fixture):
    '''
    The objective of this test is to gives more details of an object. Object numbers
    can be obtained from the results given in the Collection API.
    :return: None
    '''
    params = {"key": config.VALID_API_KEY,
              "format": "json", "culture": "en",
              "object-number": "1"
              }
    getCollectionDetailsHandler = GetCollectionDetails(config.BASE_URL)
    response = getCollectionDetailsHandler.get_collectionDetails(params)
    ResponseHandler.assert_successful_response(response)
    json_content = response.json()
    print(json_content)
    # verify if the art object and art object page (more details) about the selected collection is found
    assert 'artObject' in json_content, "Expected key 'artObject' not found in response"
    assert 'artObjectPage' in json_content, "Expected key 'artObjectPage' not found in response"

# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_get_collection_details_with_invalid_request_parameter(setup_fixture):
    '''
    The objective of this test is to check response of collection details API with an valid key
    and wrong parameter ('for', instead of 'format')
    :return:
    '''
    params = {"key": config.VALID_API_KEY, "for": "html", "culture": "en",
              "object-number": "1"}
    getCollectionDetailsHandler = GetCollectionDetails(config.BASE_URL)
    response = getCollectionDetailsHandler.get_collectionDetails(params)
    ResponseHandler.assert_unsuccessful_response_invalid_parameter(response)


def test_get_collection_details_with_invalid_collection_id(setup_fixture):
    '''
    The objective of this test is to check response of collection details API with a valid key
    and invalid collection ID "SK-R-5" instead of valid one SK-C-5
    :return: None

    '''
    params = {"key": config.VALID_API_KEY, "format": "json", "culture": "en",
              "object-number": "1"}
    getCollectionDetailsHandler = GetCollectionDetails(config.BASE_URL)
    response = getCollectionDetailsHandler.get_collection_details_invalid_collection_id(params)
    ResponseHandler.assert_unsuccessful_response_invalid_collection(response)
