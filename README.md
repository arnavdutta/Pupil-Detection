
# Pupil Detection

### Packages used

1. cv2
2. numpy
3. os
4. shutil

### Steps involved

1. Loop through all the images from the input folder
2. Convert the images from BGR colorspace to grayscale
3. Use `cv2.GaussianBlur` with kernel size (9, 9) to remove noise to an extent
4. Use `cv2.medianBlur` to reduce the noise further
5. Threshold the image to get the contours
6. Use `cv2.findContours` to find all the contours visible after thresholding and select the largest contour out of them only, as it is the pupil.
7. Get the `x`,`y`,`w`,`h` from the `cv2.boundingRect`.
8. Draw a circle using `cv2.circle`
9. Save the results in the output folder
