FROM python:3.9-slim-bookworm

RUN apt-get update -y && apt-get install -y \
    gcc g++ libffi-dev libssl-dev ffmpeg aria2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "modules/main.py"]
