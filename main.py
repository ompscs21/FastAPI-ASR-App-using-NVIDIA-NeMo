from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.model import ASRModel
from app.utils import preprocess_audio
import numpy as np

app = FastAPI()
model = ASRModel("onnx_model.onnx", "vocab.txt")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported")
    try:
        file_bytes = await file.read()
        input_features = preprocess_audio(file_bytes)
        transcription = model.transcribe(input_features)
        return JSONResponse(content={"transcription": transcription})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
