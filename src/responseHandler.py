# api_responses.py

class ResponseHandler:
    @staticmethod
    def assert_successful_response(response):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    @staticmethod
    def assert_unauthorised_response(response):
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"

    @staticmethod
    def assert_unsuccessful_response_invalid_parameter(response):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    @staticmethod
    def assert_unsuccessful_response_invalid_collection(response):
        assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
