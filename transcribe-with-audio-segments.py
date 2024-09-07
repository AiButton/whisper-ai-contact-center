import whisper

whisper_model = whisper.load_model("large")

# Function to transcribe audio
def transcribe_audio(audio_file,initial_prompt):
    result = whisper_model.transcribe(audio_file,initial_prompt=initial_prompt)
    return result['text'], result['segments']

# Example usage
if __name__ == "__main__":
    # Replace with your audio file path
    audio_file_path = "PATH_TO_YOUR_UDIO_FILE"  
    print(f"Transcribing {audio_file_path}...")
    transcription, transcription_segments = transcribe_audio(audio_file=audio_file_path,
                                                             initial_prompt="")
    for _seg in transcription_segments:
        print(f"[{_seg['start']} => {_seg['end']}]: [{_seg['text']}]")

