from datetime import datetime, timedelta

from gancio_sdk import GancioEvent, GancioSDK
from secrets import GANCIO_USER, GANCIO_PASS
from settings import GANCIO_URL


def main():
    # start_bot()
    # ns = NetworkService(GANCIO_URL)
    # ns.login(GANCIO_USER, GANCIO_PASS)
    # places = ns.get(GANCIO_PLACES)
    # print(places)
    gancio = GancioSDK(GANCIO_URL, GANCIO_USER, GANCIO_PASS)
    gancio.login()
    event = GancioEvent(
        title="Test event",
        description="This is a test event",
        # start_date is today plus one day
        start_date=datetime.now() + timedelta(days=1),
        end_date=datetime.now() + timedelta(days=2),
        tags=["test", "event"],
        place_id=3,
        image_path="test.jpg"
    )
    gancio.publish_event(event)


if __name__ == '__main__':
    main()