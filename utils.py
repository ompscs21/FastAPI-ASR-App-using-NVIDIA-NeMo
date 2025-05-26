import torchaudio
import numpy as np
import io

EXPECTED_SAMPLE_RATE = 16000

def preprocess_audio(file_bytes):
    waveform, sample_rate = torchaudio.load(io.BytesIO(file_bytes))
    if sample_rate != EXPECTED_SAMPLE_RATE:
        waveform = torchaudio.functional.resample(waveform, sample_rate, EXPECTED_SAMPLE_RATE)
    duration = waveform.size(1) / EXPECTED_SAMPLE_RATE
    if duration < 5 or duration > 10:
        raise ValueError("Audio must be between 5 to 10 seconds")
    return waveform.numpy()
