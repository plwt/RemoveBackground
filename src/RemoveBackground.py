python
import os
from rembg import remove

def remove_background(image_path):
    output_path = os.path.join(os.path.dirname(image_path), "output.png")
    with open(image_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            o.write(remove(i.read()))

def main():
    image_path = "path_to_your_image.jpg"  # Replace with the path to your image file
    remove_background(image_path)
    print("Background removed successfully. The output image is saved as output.png in the same directory as the input image.")

if __name__ == "__main__":
    main()