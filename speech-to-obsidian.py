# Libraries
import sounddevice as sd
import numpy as np
import wavio
import datetime
import whisper
from pathlib import Path
import json
from markitdown import MarkItDown

# Constants
RECORDING_DURATION = 80  # seconds
SAMPLE_RATE = 44100  # Hz
RECORDING_PATH = 'output.wav'
TRANSCRIPT_PATH = 'transcript.json'
DAILY_NOTES_PATH = 'Daily notes'

# Get today's date
today_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Record audio
print("Recording...")
audio_data = sd.rec(int(RECORDING_DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording complete.")

wavio.write(RECORDING_PATH, audio_data, SAMPLE_RATE, sampwidth=2)

# Transcribe audio
model = whisper.load_model('small')
result = model.transcribe(RECORDING_PATH, language='en', verbose=True)

# Save transcript to JSON
with open(TRANSCRIPT_PATH, "w") as file:
    json.dump(result['text'], file, indent=4)

# Convert transcript to Markdown
md = MarkItDown()  # Set to True to enable plugins
result = md.convert(TRANSCRIPT_PATH)

# Save Markdown to daily notes file
with open(f'{DAILY_NOTES_PATH}/{today_date}.md', 'w') as f:
    f.write(result.text_content)

