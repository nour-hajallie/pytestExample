import requests
from config import config


class GetCollectionDetails:
    def __init__(self, baseurl):
        """
        Initializes the GetCollectionDetails object with the base URL.
        :param baseurl: The base URL of the API.
        """
        self.baseurl = baseurl

    def get_collection_details(self, params):
        """
        Sends a GET request to retrieve collection details with a valid collection ID.
        :param params: Parameters for the GET request.
        :return: Response object from the API.
        """

        # Send the GET request with specified parameters
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT + '/' + config.VALID_COLLECTION_ID,
                                params=params)
        return response

    def get_collection_details_invalid_collection_id(self, params):
        """
        Sends a GET request to retrieve collection details with an invalid collection ID.
        :param params: Parameters for the GET request.
        :return: Response object from the API.
        """

        # Send the GET request with specified parameters
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT + '/' + config.INVALID_COLLECTION_ID,
                                params=params)

        return response
