import sounddevice as sd
import wavio
import datetime
import whisper

# Constants
SAMPLE_RATE = 44100  # Hz
RECORDING_PATH = '/Users/aidanastridge/Documents/recordings/output.wav'
DAILY_NOTES_PATH = '/Users/aidanastridge/Library/CloudStorage/GoogleDrive-astridgeaidan@gmail.com/My Drive/Public/Daily notes'

# Get today's date
today_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Function to record audio
def record_audio():
    print("Press 'Enter' to start recording, 'q' to quit.")
    input()  # Wait for user input
    
    recording_data = []
    
    while True:
        print("Recording...")
        audio_data = sd.rec(int(1 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        recording_data.extend(audio_data)
        
        user_input = input("Press 'Enter' to continue recording, 'q' to quit: ")
        if user_input.lower() == 'q':
            break
    
    print("Recording complete.")
    return recording_data

# Record audio
audio_data = record_audio()
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


