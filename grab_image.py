#!/bin/python
import os
import cv2
import shutil
import time
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"
RTSP = os.environ.get("RTSP")
LATESTIMAGE = os.environ.get("LATESTIMAGE") or 'False'


def grab_image(rtsp, location):
    vcap = cv2.VideoCapture(rtsp, cv2.CAP_FFMPEG)
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
        # create latest snapshot image, if enabled
        if LATESTIMAGE == 'True':
            latest_location = os.path.join(topdir,"latest")
            if not os.path.isdir(latest_location):
                print(f"making directory {latest_location}")
                os.makedirs(latest_location)
            print(f"saving to {latest_location}/snapshot.png")
            shutil.copy(location, f"{latest_location}/snapshot.png")
    else:
        print("Failed to grab image")


if __name__ == '__main__':
    main()

