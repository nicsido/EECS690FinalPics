import cv2
from PIL import Image


# Open the image file
image = Image.open('imagePin1.png')


# Set the new maximum width and height for the image
max_width = 1050
max_height = 1050


# Get the original size of the image
width, height = image.size


# Calculate the new dimensions while maintaining the aspect ratio
if width > height:
    new_width = max_width
    new_height = int(height * (max_width / width))
else:
    new_height = max_height
    new_width = int(width * (max_height / height))


# Resize the image using the ANTIALIAS filter
resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)


# Save the resized image as a new file
resized_image.save('resized_image.png')


# Load the resized image
img = cv2.imread('resized_image.png')


# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Apply a threshold to the image to binarize it
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# Find the contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Create a copy of the image for drawing
img_copy = img.copy()


# Loop over the contours
for cnt in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(cnt)


    # Calculate the aspect ratio of the bounding rectangle
    aspect_ratio = float(w)/h


    # If the aspect ratio is not within a certain range, it is likely a defective pin
    if aspect_ratio < 0.5 or aspect_ratio > 2.0:
        # Draw a red rectangle around the bounding rectangle
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 0, 255), 2)


# Show the image with the detected defects
cv2.imshow('Defective pins', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()