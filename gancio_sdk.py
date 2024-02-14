import datetime

from network_endpoints import GANCIO_ADD_EVENT, GANCIO_PLACES
from network_service import NetworkService


class GancioEvent:
    def __init__(self,
                 title: str,
                 description: str,
                 start_date: datetime.datetime,
                 end_date: datetime.datetime,
                 tags: list[str],
                 place_id: int,
                 image_path: str):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tags = tags
        self.place_id = place_id
        self.image_path = image_path

    # Event to json
    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "start_datetime": int(self.start_date.timestamp()),
            "end_datetime": int(self.end_date.timestamp()),
            "tags[]": self.tags,
            "place_id": self.place_id,
            "image_path": self.image_path
        }


class GancioSDK:

    def __init__(self, api_endpoint, user, password):
        self.api_endpoint = api_endpoint
        self.network_service = NetworkService(api_endpoint)
        self.user = user
        self.password = password

    def login(self):
        self.network_service.login(self.user, self.password)

    def publish_event(self, event: GancioEvent):
        data = event.to_json()
        self.network_service.post_multipart(GANCIO_ADD_EVENT, data, event.image_path)

    def places(self):
        return self.network_service.get(GANCIO_PLACES)
