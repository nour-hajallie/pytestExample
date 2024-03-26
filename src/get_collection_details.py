import requests
from config import config


class GetCollectionDetails:
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_collectionDetails(self, params):
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT +'/'+ config.VALID_COLLECTION_ID, params=params)
        return response

    def get_collection_details_invalid_collection_id(self,params):
        response = requests.get(url=self.baseurl + config.GET_COLLECTION_END_POINT +'/'+ config.INVALID_COLLECTION_ID, params=params)
        return response