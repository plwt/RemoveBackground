import os
from rembg import remove
from PIL import Image
import os


def remove_background(image_path):
    output_path = os.path.join(os.path.dirname(image_path), "output.png")
    with open(image_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            o.write(remove(i.read()))
    output=Image.open("/opt/RemoveBackground/output.png")
    hmat,wmat = output.size
    background=Image.open("opt/RemoveBackground/background.png")
    resizebackground=background.resize((hmat,wmat))
    resizebackground.paste (output,box=(0,0),background=output)
    resizebackground.save(image_path + "complete.png")

def main():
    image_path = "/opt/RemoveBackground/image.jpg"
    remove_background(image_path)
    print("Background removed successfully. The output image is saved as output.png in the same directory as the input image.")

if __name__ == "__main__":
    main()
