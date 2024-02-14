import json
from typing import BinaryIO

from network_endpoints import LOGIN_PATH
from secrets import GANCIO_USER, GANCIO_PASS
from settings import logger
import requests


class NetworkService:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'python_network_service/0.0.1'})
        self.session.hooks['response'].append(lambda r, *args, **kwargs: self.get_new_token(r, *args, **kwargs))
        self.refresh_token = None

    def _save_auth(self, response):
        parsed = json.loads(response.text)
        access_token = parsed["access_token"]
        self.refresh_token = parsed["refresh_token"]
        self.session.headers.update({'Authorization': f'Bearer {access_token}'})

    def get_new_token(self, response, *args, **kwargs):
        if response.status_code == 401:
            logger.info("Fetching new token as the previous token expired")
            # todo: implement refresh token function
            self.login(GANCIO_USER, GANCIO_PASS)
            # session.headers.update({"Authorization": f"Bearer {token}"})
            # r.request.headers["Authorization"] = session.headers["Authorization"]
            return self.session.send(response.request, verify=False)

    def login(self, user, password):
        """Stores the tags and asks publish the event."""
        logger.info("Requesting new token")
        oauth_url = f"{self.base_url}{LOGIN_PATH}"

        # Send the POST request with the event object as JSON payload
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            "client_id": "self",
            "password": password,
            "username": user,
            "grant_type": "password"
        }
        response = self.session.post(f"{oauth_url}", headers=headers, data=payload)
        if response.status_code == 200:
            self._save_auth(response)
            logger.info("New token got")

        else:
            logger.info("Request token failed")
            logger.info(response.text, response.status_code)

    def get(self, endpoint, params=None):
        """Make a GET request to a specific endpoint."""
        try:
            response = self.session.get(f'{self.base_url}{endpoint}', params=params)
            response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
            return response.json()  # Returns the json-encoded content of a response, if any
        except requests.exceptions.RequestException as e:
            logger.error(f'An error occurred: {e}')
            raise e

    def post(self, endpoint, data=None):
        """Make a POST request to a specific endpoint."""
        logger.info(f"Post {endpoint} with data {data}")

        try:
            response = self.session.post(f'{self.base_url}{endpoint}', json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'An error occurred: {e}')
            raise e

    def post_multipart(self, endpoint, data, file_path: str):
        """Make a POST request to a specific endpoint."""
        logger.info(f"Post multipart {endpoint} with data {data}, {file_path}")

        files = {
            'image': (file_path, open(file_path, 'rb')),
        }

        try:
            response = self.session.post(f"{self.base_url}{endpoint}", data=data, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'An error occurred: {e}')
            raise e



