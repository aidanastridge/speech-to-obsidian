# Libraries
import sounddevice as sd
import numpy as np
import wavio
import datetime
import whisper
from pathlib import Path
import json
from markitdown import MarkItDown

# Get today's date
today_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Paths
recording = 'output.wav'

# Parameters
duration = 10  # seconds
sample_rate = 44100  # Hz

# Record audio
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording complete.")

wavio.write(recording, audio_data, sample_rate, sampwidth=2)

model = whisper.load_model('tiny')
path = Path(recording)

result = model.transcribe(str(path), language='en', verbose=True)

# Dump the results to a JSON file
with open('transcript.json', "w") as file:
    json.dump(result['text'], file, indent=4)

md = MarkItDown() # Set to True to enable plugins
result = md.convert('transcript.json')

with open(f'{today_date}.md', 'w') as f:
    f.write(result.text_content)

