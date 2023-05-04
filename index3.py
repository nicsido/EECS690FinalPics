import cv2
import numpy as np

# Load the image
image = cv2.imread('imagePin5.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary mask
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find the contours of the pins
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Initialize variables for tracking the maximum angle and the corresponding contour
max_angle = 0
max_contour = None

# Iterate over the contours and analyze their orientation
for contour in contours:
    # Calculate the minimum bounding box around the contour
    rect = cv2.minAreaRect(contour)
    # Calculate the angle of the minimum bounding box
    angle = rect[2]
    # Draw a bounding box around the contour
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    # Check if the angle is greater than the maximum angle seen so far
    if abs(angle) > max_angle:
        max_angle = abs(angle)
        max_contour = contour

# Draw a bounding box around the contour with the largest angle
if max_contour is not None:
    rect = cv2.minAreaRect(max_contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
    cv2.putText(image, "Largest angle: {} degrees".format(max_angle), (box[0][0], box[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the result
cv2.imshow('Largest angle pin detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
