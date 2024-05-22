# RemoveBackground

Here is a Python program that uses the `rembg` library to remove the background from an image saved in a file. The file path is hardcoded in the program:

```python
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
```

Replace `"path_to_your_image.jpg"` with the actual path to the image file you want to remove the background from.

To use this program, you need to have the `rembg` library installed. You can install it using pip:

```
pip install rembg
```

If you want to use a virtual environment (venv), you can create one and activate it before installing the `rembg` library:

```
python -m venv myenv
myenv\Scripts\activate
pip install rembg
```

Replace `myenv` with the name you want to give to your virtual environment.

After installing the `rembg` library, you can run the Python program.
