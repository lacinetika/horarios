from datetime import datetime, timedelta

from calcular_siguiente_asamblea import get_activities_between_dates, Activity, next_activity_from_date
from gancio_sdk import GancioSDK, GancioEvent
from secrets import GANCIO_PASS, GANCIO_USER
from settings import GANCIO_URL, GANCIO_IMG, GANCIO_DESCRIPTION, GANCIO_TITLE, logger, GANCIO_TAGS, GANCIO_PLACE_ID


# Function to check if a given date is yesterday
def is_yesterday(date):
    # Current date and time
    now = datetime.now()
    # Yesterday's date and time
    yesterday = now - timedelta(days=1)
    return date.date() == yesterday.date()


def publish_activity(activity: Activity):
    gancio = GancioSDK(GANCIO_URL, GANCIO_USER, GANCIO_PASS)
    gancio.login()
    event = GancioEvent(
        title=GANCIO_TITLE,
        description=GANCIO_DESCRIPTION,
        start_date=activity.date,
        end_date=activity.date + timedelta(hours=1),
        tags=GANCIO_TAGS,
        place_id=GANCIO_PLACE_ID,
        image_path=GANCIO_IMG
    )
    gancio.publish_event(event)

    logger.info(f"Published gancio event: {event.title}")


def publish_if_yesterday():
    today_date = datetime.now()
    activity_list = get_activities_between_dates(today_date)
    # get the previous last activity
    last_activity = activity_list[len(activity_list) - 2]
    if is_yesterday(last_activity.date):
        next_activity = activity_list[len(activity_list) - 1]
        logger.info(f"Publishing for publish_if_yesterday {next_activity}")
        publish_activity(next_activity)
    else:
        logger.info(f"No event to publish for publish_if_yesterday")


def publish_next():
    logger.info("Publishing next event")
    activity = next_activity_from_date(datetime.now())
    publish_activity(activity)


if __name__ == "__main__":
    logger.info("Publishing if yesterday")
    publish_if_yesterday()
