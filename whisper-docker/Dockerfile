# Use an official Python runtime as a parent image
FROM python:3.9-slim



# Install required packages
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy the pre-downloaded Whisper model into the container
COPY ./whisper /root/.cache/whisper

# Set the working directory
WORKDIR /app

COPY ./sounds/Logistics.wav /app

# Copy your application code to the container
COPY main.py /app

# Install required packages
RUN pip install --no-cache-dir openai-whisper fastapi uvicorn torchaudio librosa


# Command to run your application
CMD ["python", "main.py"]
