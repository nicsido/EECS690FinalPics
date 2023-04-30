import cv2
import numpy as np


# Load the image
img = cv2.imread('imagePin1.png')


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