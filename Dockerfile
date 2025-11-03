FROM python:3.9-slim-buster

# Install required system packages
RUN apt-get update -y && apt-get install -y \
    gcc g++ libffi-dev libssl-dev ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the bot
CMD ["python", "modules/main.py"]
