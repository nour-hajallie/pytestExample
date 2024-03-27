import requests
from config import config


class GetCollection:
    def __init__(self, baseurl):
        """
        Initializes the GetCollection object with the base URL.
        :param baseurl: The base URL of the API.
        """
        self.baseurl = baseurl

    def get_collection(self, params):
        """
        Sends a GET request to retrieve collection data.
        :param params: Parameters for the GET request.
        :return: Response object from the API.
        """

        # Send the GET request with specified parameters
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT, params=params)
        return response
