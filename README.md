# ztcode
ztcode stands for (Zhvan's Trinary Code). It's a simple type of 2D Barcode, that uses trinary instead of binary. 
## Data Representation
ztcode uses 3 colors, shown below. <br>
White = 0<br>
Black = 1<br>
Green = 2
## Encoding
All it really does, is convert the text to trinary, create an image, then it puts the green, white and black pixels in order on the image, using pillow. 
