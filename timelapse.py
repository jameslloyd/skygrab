import ffmpeg
from datetime import datetime, timedelta
import shutil
import os

def create_timelapse_video(location,outputdir,filename,res='1280:720',framerate = 25):
    outputfile = f'{outputdir}/{filename}-{res.replace(":","_")}.webm'
    if os.path.exists(outputfile):
        print(f"Removing existing {outputfile}")
        os.remove(outputfile)
    (
        ffmpeg.input(f'{location}/*.png', pattern_type='glob', framerate=framerate)
        .filter('deflicker',mode='pm',size=10)
        .filter('scale',size=res)
        .output(outputfile, crf=20, preset='slower', pix_fmt='yuv420p', vcodec='libvpx-vp9')
        .run()
    )    

def main():
    yesterday = datetime.now() - timedelta(-1) # yesterday
    datetoprocess = datetime.strftime(yesterday, '%Y/%m/%d')
    filename = datetime.strftime(yesterday,'%Y%m%d')
    if not os.path.isdir(datetoprocess):
        print(f"images/{datetoprocess} path does not exist")
    else:
        create_timelapse_video(datetoprocess,'.','timelapse')
    


if __name__ == '__main__':
    main()