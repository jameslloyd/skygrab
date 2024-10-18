# Grab regular RTSP pictures and make a timelapse from them

replace the X's

```
docker run -v /home/james/testing:/app/images -e INTERVAL=X -e RTSP="rtsp://X.X.X.X/ch0_0.h264" jameslloyd/skygrab
```
Will generate an webm timelapse for the previous day at 00:05 


### Config Variables

- INTERVAL (seconds, default=60)
- RTSP (URL, required, default=None)
- LATESTIMAGE (True/False, create latest image in /latest/ dir, default=False)
