#!/bin/python
import os
import cv2

vidcap = cv2.VideoCapture("yeet.mp4")

path = "/tmp"

count=0
while True:
	success, image = vidcap.read()
	if not success:
		break
	cv2.imwrite(os.path.join(path, "{:d}.png".format(count)), image)
	count += 1
