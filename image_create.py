import os
import time
from datetime import datetime

from calcular_siguiente_asamblea import next_activity_from_date, Activity
from settings import logger, NEXT_ACT_IMAGE
from utils.image import create_image

template = """<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Cinètika proxima assamblea</title>
</head>
<body>
    <img src="{image}" alt="Proxima ass">
</body>
</html>
"""

def add_string_before_extension(file_name, string_to_add):
    # Split the file name into name and extension
    name, extension = os.path.splitext(file_name)
    # Add the string to the file name before the extension
    new_file_name = f"{name}{string_to_add}{extension}"
    return new_file_name

def create_next_activity_image():
    activity: Activity = next_activity_from_date(datetime.now())
    image = create_image(activity.img_repr)
    directory_path = os.path.dirname(NEXT_ACT_IMAGE)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    image.save(NEXT_ACT_IMAGE)
    # Saving to a file
    with open(directory_path + '/index.html', 'w') as file:
        file.write(template.format(image=f"{NEXT_ACT_IMAGE}?nocache={int(time.time())}"))



if __name__ == "__main__":
    logger.info("Creating image")
    create_next_activity_image()
