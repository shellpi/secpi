from imutils.object_detection import non_max_suppression
import cv2
import numpy as np

# FUNCTION TO DETECT IF THERE ARE PEOPLE IN AN IMAGE #
def detect_if_people(img) -> bool:
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	image = cv2.imread(img)
	image = cv2.resize(image, (min(800, image.shape[1]), min(600, image.shape[0])), interpolation = cv2.INTER_LINEAR)
	(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(0, 0), scale=1.01)

	if len(rects) == 0:
		return False
	else:
		return True
