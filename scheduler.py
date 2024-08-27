import os
import sched
import time
import threading
import logging
from datetime import datetime, timedelta
from grab_image import main as grab_image
from timelapse import main as create_timelapse
from dotenv import load_dotenv

load_dotenv()


def grab_camera_image_task():
    grab_image()

def create_timelapse_task():
    # ... (Your second function's logic here)
    create_timelapse()
    print("Function 2 executed!")

def schedule_task_1(scheduler, interval):
    # Create and start a thread for the first function
    thread1 = threading.Thread(target=grab_camera_image_task)
    thread1.start()

    # Schedule the task to run again after the specified interval
    scheduler.enter(interval, 1, schedule_task_1, (scheduler, interval))

def schedule_task_2_at_specific_time(scheduler):
    # Get the current time
    now = datetime.now()

    # Define the target time (e.g., 3:00 PM)
    target_time = now.replace(hour=00, minute=5, second=0, microsecond=0)

    # If the target time has already passed today, schedule for tomorrow
    if target_time < now:
        target_time += timedelta(days=1)

    # Calculate the delay in seconds until the target time
    delay = (target_time - now).total_seconds()

    # Schedule the task to run at the specific time (without executing immediately)
    scheduler.enter(delay, 1, execute_task_2_and_reschedule, (scheduler,))

def execute_task_2_and_reschedule(scheduler):
    # Create and start a thread for the second function
    thread2 = threading.Thread(target=create_timelapse_task)
    thread2.start()

    # Reschedule the task for the next day at the same specific time
    schedule_task_2_at_specific_time(scheduler)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    scheduler1 = sched.scheduler(time.time, time.sleep)
    scheduler2 = sched.scheduler(time.time, time.sleep)

    # Get the schedule interval from the environment variable (in seconds)
    interval1 = int(os.environ.get('INTERVAL', 60))  # Default to 60 seconds if not set

    # Schedule the initial task executions
    schedule_task_1(scheduler1, interval1)
    schedule_task_2_at_specific_time(scheduler2)

    # Start both schedulers
    threading.Thread(target=scheduler1.run).start()
    threading.Thread(target=scheduler2.run).start()