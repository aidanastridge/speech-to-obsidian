from datetime import datetime

# Get today's date
today = datetime.now()

# Format the date in YMD format
ymd_format = today.strftime("%Y-%m-%d")

from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("transcription.docx")
print(result.text_content)

