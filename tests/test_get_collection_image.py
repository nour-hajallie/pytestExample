from unittest import TestCase

import pytest

from config import config
from src.getCollectionImage import GetCollectionImage
from src.responseHandler import ResponseHandler


@pytest.fixture
def setup_fixture():
    print("This is setup_fixture for get collection image details")
    # Code to set up resources or perform setup actions
    yield
    print("Teardown actions if needed")


def test_get_collection_image_with_valid_key(setup_fixture):
    '''
    The objective of this test is to check response of image details API with an valid key
    :return:
    '''
    params = {"key": config.VALID_API_KEY, "object-number": "1"}
    getCollectionImageHandler = GetCollectionImage(config.BASE_URL)
    response = getCollectionImageHandler.get_collection_image(params)
    ResponseHandler.assert_successful_response(response)
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


def test_get_collection_image_with_invalid_key(setup_fixture):
    '''
    The objective of this test is to check response of image details API with an invalid key
    :return:
    '''
    params = {"key": config.INVALID_API_KEY, "object-number": "1"}
    getCollectionImageHandler = GetCollectionImage(config.BASE_URL)
    response = getCollectionImageHandler.get_collection_image(params)
    ResponseHandler.assert_unauthorised_response(response)


# Unexpected behaviour test
@pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_get_collection_image_with_invalid_request_parameter(setup_fixture):
    '''
    The objective of this test is to check response of image details API with an valid key
    and invalid parameter ,, "obje" instead of "object-number"
    :return:
    '''
    params = {"key": config.VALID_API_KEY, "obje": "1"}
    getCollectionImageHandler = GetCollectionImage(config.BASE_URL)
    response = getCollectionImageHandler.get_collection_image(params)
    ResponseHandler.assert_unsuccessful_response_invalid_parameter(response)



def test_get_collection_image_with_invalid_collection_id(setup_fixture):
    '''
    The objective of this test is to check response of collection image API with a valid key
    and invalid collection ID "SK-R-5" instead of valid one SK-C-5
    :return:
    '''
    params = {"key": config.VALID_API_KEY, "object-number": "1"}
    getCollectionImageHandler = GetCollectionImage(config.BASE_URL)
    response = getCollectionImageHandler.get_collection_image_invalid_collection_id(params)
    ResponseHandler.assert_unsuccessful_response_invalid_collection(response)
