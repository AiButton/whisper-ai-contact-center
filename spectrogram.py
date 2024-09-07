import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
audio_path = 'PATH_TO_YOUR_AUDIO_FILE'
y, sr = librosa.load(audio_path, sr=None)

# Compute the Mel spectrogram
n_mels = 80  # Number of Mel bands, typically 80 for Whisper
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)

# Convert to log scale (log-Mel spectrogram)
S_db = librosa.power_to_db(S, ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel', fmax=sr/2)
plt.colorbar(format='%+2.0f dB')
plt.title('Log-Mel Spectrogram')
plt.show()
