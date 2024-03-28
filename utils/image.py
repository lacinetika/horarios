from PIL import Image, ImageDraw, ImageFont


def create_image(text:str) -> Image:

    # Create an image with RGB mode and white background
    width, height = 600, 100
    image = Image.new("RGB", (width, height), "white")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define the text to be added and the font properties
    font = ImageFont.truetype("DejaVuSans.ttf", 40)  # You may need to adjust the path to the font


    # Calculate the width and height of the text to be added
    _, _, tw, th = draw.textbbox((0, 0), text, font=font,)

    # Calculate the X, Y position of the text
    x = (width - tw) / 2
    y = (height - th) / 2

    # Add text to image
    draw.text((x, y), text, font=font, fill =(0, 0, 0))

    # Save the image
    return image
    # image.save("sample_image.png")

