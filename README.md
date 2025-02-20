### Speech to Obsidian

#### Thesis

Records and transcribes daily-note into Obsidian vault.

#### Libraries
- [sounddevice](https://python-sounddevice.readthedocs.io/en/0.5.1/) 
- [wavio](https://github.com/WarrenWeckesser/wavio)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [openai-whisper](https://github.com/openai/whisper)
- [json](https://docs.python.org/3/library/json.html#module-json)
- [markitdown](https://github.com/microsoft/markitdown)

#### Order of Operations

1. Record
2. Export to WAV
3. Transcribe
4. Export to JSON
5. Convert to Markdown
6. Places it in Obsidian vault.

#### Questions? 
Why export to json instead of straight to Markdown?
<br>
I am checking if the conversion is correct.

#### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/aidanastridge/speech-to-obsidian/blob/main/LICENSE) file for details.
