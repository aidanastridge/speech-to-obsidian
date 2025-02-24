import sounddevice as sd
import wavio
import datetime
import whisper

# Constants
RECORDING_DURATION = 40  # seconds
SAMPLE_RATE = 44100  # Hz
RECORDING_PATH = '/Users/aidanastridge/Documents/recordings/output.wav'
DAILY_NOTES_PATH = '/Users/aidanastridge/Library/CloudStorage/GoogleDrive-astridgeaidan@gmail.com/My Drive/Public/Daily notes'

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

# Create Markdown content
markdown_content = f"""
Tags: #tasks

{result['text']}
"""

# Save Markdown to daily notes file
with open(f'{DAILY_NOTES_PATH}/{today_date}.md', 'w') as f:
    f.write(markdown_content)

print("Markdown file saved successfully!")

