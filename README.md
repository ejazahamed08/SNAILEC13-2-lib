# SNAILEC13-2-lib
# Turtle drawing to PNG Exporter

This script draws a square and circle and automatically saves the drawing as a png.

# Libraries Used

This project relies on two main libraries to render and convert the graphics:
* **`turtle`** (Built into Python): Opens the graphical window and handles the vector drawing mechanics and exports the drawing as a '.eps' file.
* **`Pillow`** (External Library): After the drawing is done reads the '.eps' file and converts it into a '.png' image.

# needed libaries installed (macOS)

Before running the script, you need the following libararies installed on your machine:

1. brew install python-tk
2. brew install ghostscript
3. pip install pillow

# how to run

python3 my_drawing.py

# output

should get a drawing.png with a circle and square

# what it cant do yet

direct png export, turtle doesnt support exporting the drawing into png rather it comes out as a .epg and then we use
pillow to convert it to .png
