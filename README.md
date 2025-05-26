# FastAPI-ASR-App-using-NVIDIA-NeMo
This project implements an automatic speech recognition (ASR) web service using the stt_hi_conformer_ctc_medium Hindi language model from NVIDIA NeMo. The application uses FastAPI to expose a /transcribe API endpoint that accepts .wav files (5–10 seconds, 16kHz), transcribes the speech to text, and returns the result as JSON.
