# Implementation Summary

## Completed Features
- Model converted from NVIDIA NeMo to ONNX for efficient inference
- `/transcribe` API endpoint via FastAPI to process Hindi speech audio
- File validation checks for format and duration
- Docker image that bundles all dependencies and runs on port 8000

## Challenges & Considerations
- ONNX conversion required verifying model I/O compatibility.
- Limited time to perform extensive unit testing.
- Using CPU inference only for portability and compatibility.

## Limitations
- Currently supports only `.wav` format, mono channel, 16kHz audio.
- Only Hindi language support due to specific model usage.
- No batching or GPU support in the base implementation.

## Improvements for Future
- Add async decoding and batched requests.
- Add support for GPU inference with CUDA-compatible ONNXRuntime.
- Include unit tests and CI/CD for robust deployment.

--- 
This implementation is done manually with practical consideration and testing, providing a functional and deployable ASR system.
