import sounddevice as sd
import numpy as np
import wavio
import datetime

recording = 'output.wav'

# Parameters
duration = 5  # seconds
sample_rate = 44100  # Hz

# Record audio
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording complete.")

wavio.write(recording, audio_data, sample_rate, sampwidth=2)

