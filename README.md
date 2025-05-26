# FastAPI-ASR-App-using-NVIDIA-NeMo
This project implements an automatic speech recognition (ASR) web service using the stt_hi_conformer_ctc_medium Hindi language model from NVIDIA NeMo. The application uses FastAPI to expose a /transcribe API endpoint that accepts .wav files (5–10 seconds, 16kHz), transcribes the speech to text, and returns the result as JSON.

This project provides a simple automatic speech recognition (ASR) web service using the `stt_hi_conformer_ctc_medium` model from NVIDIA NeMo. The application uses FastAPI for serving and ONNX for optimized inference.

## Features
- Transcribe Hindi `.wav` files (5–10 seconds)
- Model optimized with ONNX Runtime
- Dockerized for easy deployment
- Input validation for file type and duration

## Setup Instructions

### Build Docker Image
```bash
docker build -t nemo-asr .
```

### Run the Docker Container
```bash
docker run -p 8000:8000 nemo-asr
```

### Example Request using `curl`
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test_audio.wav"
```

## Notes
- Ensure input `.wav` files are mono, 16kHz, and between 5–10 seconds.
- For production, consider mounting a model volume and adding logging.
