from fastapi import FastAPI, UploadFile, File,HTTPException
from pydantic import BaseModel
import whisper
import base64
import io, os
import torchaudio
import torch
from starlette.responses import JSONResponse
import numpy as np
import librosa

app = FastAPI()

# Load the Whisper model
model = whisper.load_model("medium")

class AudioData(BaseModel):
    audio: str  # base64 encoded audio

def decode_base64_to_audio(base64_str: str) -> torch.Tensor:
    audio_data = base64.b64decode(base64_str)
    audio_buffer = io.BytesIO(audio_data)
    waveform, sample_rate = torchaudio.load(audio_buffer, normalize=True)
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
    return waveform



@app.post("/transcribe/")
async def transcribe(audio_data: AudioData):
    try:
        # Decode base64 string
        audio_bytes = base64.b64decode(audio_data.audio)

        # Use in-memory file-like object
        audio_file_like = io.BytesIO(audio_bytes)

        # Load audio data into a NumPy array
        # Note: Specify the sampling rate if needed
        audio_np, _ = librosa.load(audio_file_like, sr=None)

        # Transcribe using Whisper
        result = model.transcribe(audio_np)

        transcripts = {}
        transcripts['segments'] = []
        transcripts['language'] = result['language']
        seq = 1
        for _seg in result['segments']:
            print(f"[{_seg['start']} ===> {_seg['end']}]: [{_seg['text']}]")
            segment = {}
            segment['seq_no'] = seq
            segment['start'] = _seg['start']
            segment['end'] = _seg['end']
            segment['text'] = _seg['text']
            transcripts['segments'].append(segment)
            seq = seq + 1

        return {"transcription": transcripts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
