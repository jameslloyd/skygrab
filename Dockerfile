FROM python:3.8-slim-buster

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /app

# Copy your Python script into the container
COPY * .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Start the startup script
CMD ["python","scheduler.py"] 
