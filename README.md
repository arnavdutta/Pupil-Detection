
# Pupil Detection

### Packages used

1. OpenCV
2. Numpy
3. os
4. shutil

### Steps involved for detecting pupil from images

1. Loop through all the images from the input folder
2. Convert the images from BGR colorspace to grayscale
3. Use `cv2.GaussianBlur` with kernel size (9, 9) to remove noise to an extent
4. Use `cv2.medianBlur` to reduce the noise further
5. Threshold the image to get the contours
6. Use `cv2.findContours` to find all the contours visible after thresholding and select the largest contour out of them only, as it is the pupil.
7. Get the `x`,`y`,`w`,`h` from the `cv2.boundingRect`.
8. Draw a circle using `cv2.circle`
9. Save the results in the output folder

### Steps involved for detecting pupil from a video of an eye

1. Capture the video file using `cv2.VideoCapture` 
2. Loop the video continuously and save the frames of the video using `read()`
3. Get the exact area of the eye (ROI) from the whole frame.
4. Convert the ROI region into Grayscale then use GaussianBlur as well as medianBlur to reduce the noise.
5. Threshold the ROI region to get the contours and select only the largest contour as it will be pupil.
6. Once, contour is detected using `cv2.findContours`, get the `x`,`y`,`w`,`h` from the `cv2.boundingRect`
7. Draw a circle using `cv2.circle`

`NOTE`: use `cap.set(cv2.CAP_PROP_POS_FRAMES, 0)` to loop back the video from beginning otherwise, it will throw error as there is no frame to capture.

`NOTE`: At the end `release()` the video file.
