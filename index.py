import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Input image name here, opens the image.
img = Image.open('image2.png')

# Convert image to grayscale
img = img.convert('L')

# Increase contrast to make text more visible
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)

# Apply median filter to remove noise
img = img.filter(ImageFilter.MedianFilter())

# Apply thresholding to convert image to black and white
img = img.point(lambda x: 0 if x<150 else 255, '1')

# Apply dilation to make text thicker and easier to recognize
img = img.filter(ImageFilter.MaxFilter(3))

# Recognize the text and then set it equal to the value "text"
text = pytesseract.image_to_string(img)

# Print the recognized text
print(text)