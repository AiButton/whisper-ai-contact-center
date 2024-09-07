import base64

def encode_audio_to_base64(file_path: str) -> str:
    """
    Encode an audio file to a base64 string.
    
    :param file_path: Path to the audio file.
    :return: Base64 encoded string of the audio file.
    """
    with open(file_path, "rb") as audio_file:
        # Read the audio file as bytes
        audio_bytes = audio_file.read()
        # Encode the bytes to base64
        encoded_audio = base64.b64encode(audio_bytes)
        # Convert the base64 bytes to a string
        encoded_audio_str = encoded_audio.decode('utf-8').replace('\r', '')
        return encoded_audio_str

if __name__ == "__main__":
    # Replace 'path_to_your_audio_file.wav' with the path to your audio file
    file_path = '../sounds/languages-simith.wav'
    base64_encoded_audio = encode_audio_to_base64(file_path)
    print(base64_encoded_audio)

