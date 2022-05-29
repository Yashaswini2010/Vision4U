import face_recognition 
import cv2
import numpy as numpy

#this is a demo of running face recognition on live video. It includes some basic performance tweaks
#1. Process each video frame at 1/4 resolution 
#2. Only detect faces in every other frame of video

#get a reference to webcom #0 (the default one)
video_capture = cv2.VideoCapture(0)