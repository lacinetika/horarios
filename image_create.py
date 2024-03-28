import os
from datetime import datetime

from calcular_siguiente_asamblea import next_activity_from_date, Activity
from settings import logger, NEXT_ACT_IMAGE
from utils.image import create_image


def create_next_activity_image():
    activity: Activity = next_activity_from_date(datetime.now())
    image = create_image(activity.img_repr)
    directory_path = os.path.dirname(NEXT_ACT_IMAGE)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    image.save(NEXT_ACT_IMAGE)



if __name__ == "__main__":
    logger.info("Creating image")
    create_next_activity_image()
