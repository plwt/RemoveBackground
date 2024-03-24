# install required packages
from PIL import Image
from rembg import remove
import os
import sys
from pathlib import Path


# Welcome message
def welcome():
    print("""
    Welcome to RemoveBackground
    """)

welcome()


# Remove Backgound
def removebackground():
    # Ask the user to confirm the image has been saved
    Gonogo=input("Have you saved the file to be edited to the RemoveBackground folder in your user documents with filename image.jpg?(y/n)")
    
    if Gonogo=="n":
        print("Please save the image to be edited to the RemoveBackground folder in your user documents with the filename image.jpg and run RemoveBackground again.")
          

    elif Gonogo=="y":
        
        from pathlib import Path
        home_path = str(Path.home())
        
        # Set in-bound file path
        input_path = (home_path + '/RemoveBackground/image.jpg')
        
        # Set out-bound file path
        output_path = (home_path + '/RemoveBackground/output.png')

        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)

        # Confirm the edited image has been saved
        print("Your edited file has been saved to the RemoveBackground folder in your user documents with the filename output.png.  Thank you for using RemoveBackground")
    else:
        print("Please try again.")

removebackground()