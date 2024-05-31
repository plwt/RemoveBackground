import os
from rembg import remove
from PIL import Image
import os


def remove_background(image_path):
    output_path = os.path.join(os.path.dirname(image_path), "output.png")
    with open(image_path, "rb") as i:
        with open(output_path, "wb") as o:
            o.write(remove(i.read()))

    # Open the images
    output_image = Image.open("output.png")
    background_image = Image.open("background.png")

    # Resize the background image to match the output image size
    background_image = background_image.resize(output_image.size)

    # Create a new image with the same size as the output image
    new_image = Image.new("RGB", output_image.size)

    # Paste the background image onto the new image
    new_image.paste(background_image, (0, 0))

    # Paste the output image onto the new image
    new_image.paste(output_image, (0, 0), output_image)

    # Save the new image
    new_image.save("combined_image.png")


def main():
    image_path = "/opt/RemoveBackground/image.jpg"
    remove_background(image_path)
    print(
        "Background removed successfully. The output image is saved as output.png in the same directory as the input image."
    )


if __name__ == "__main__":
    main()
