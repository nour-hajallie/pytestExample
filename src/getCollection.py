import requests
from config import config


class GetCollection:
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_collection(self, params):
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT, params=params)
        return response