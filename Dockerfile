FROM python:3.11-slim

# Install only the essential system packages
RUN apt-get update && apt-get install -y \
    libzbar0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libglib2.0-0 \
    ffmpeg \
    wget \
    unzip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["functions-framework", "--target=qrreader", "--port=8080"]
