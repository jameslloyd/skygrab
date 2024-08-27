#!/bin/python
import os
import cv2
import shutil
import time
from dotenv import load_dotenv

load_dotenv()

RTSP = os.environ.get("RTSP")

def grab_image(rtsp, location):
    vcap = cv2.VideoCapture(RTSP)
    if vcap.isOpened():
        ret, frame = vcap.read()
        cv2.imwrite(location, frame)
        return True
    else:
        return False
    
def main():
    topdir = 'images'
    filename = time.strftime("%Y%m%d-%H%M%S")
    dirpath = time.strftime("%Y/%m/%d/")
    if not os.path.isdir(os.path.join(topdir,dirpath)):
        os.makedirs(os.path.join(topdir,dirpath))
    location = os.path.join(topdir,dirpath,filename+'.png')
    if grab_image(RTSP,location):
        print(f"{location} grabbed successfully")
    else:  
        print("Failed to grab image")

if __name__ == '__main__':
    main()

