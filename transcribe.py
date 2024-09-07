import whisper
# Load the desired model (e.g., 'base', 'small', 'medium', 'large')
model = whisper.load_model("medium.en")  
# Now you can use the model to transcribe audio
result = model.transcribe("PATH_TO_YOUR_AUDIO_FILE")
print(result["text"])
