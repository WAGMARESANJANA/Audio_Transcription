# 🗣️ Audio Transcription

This Python project allows you to:

* Convert **text into speech** and save it as a WAV file.
* **Transcribe speech** from a WAV file back into text.

It uses the `pyttsx3` library for offline text-to-speech synthesis and the `speech_recognition` library for audio transcription via Google's Web Speech API.

##  Features

* 🔊 **Text-to-Speech**: Convert any string into a spoken audio WAV file.
* ✍️ **Speech-to-Text**: Transcribe spoken content from WAV files using Google's speech recognition.
* 🧪 **End-to-End Demo**: A simple example that demonstrates both functionalities.

##  Requirements

Install the required packages using pip:

```bash
pip install pyttsx3 SpeechRecognition
```

> **Note:** For Windows users, you might also need `pypiwin32`.
> For Linux/macOS, ensure you have the appropriate audio playback libraries.

## 📂 File Structure

```
.
├── audio_transcription.py  # Main script
└── example.wav             # Example audio (generated by script)
```

## How to Use

Run the script directly:

```bash
python audio_transcription.py
```

### What it does:

1. Converts the sample sentence `"Hello, my name is Alex and I love programming."` into speech.
2. Saves the speech audio as `example.wav`.
3. Reads back `example.wav` and transcribes it into text using Google Speech Recognition.

## Function Descriptions

### `text_to_speech(text: str, filename: str)`

Converts a string of text into a `.wav` audio file.

* **Parameters:**

  * `text`: The input string to be spoken.
  * `filename`: Output filename for the audio.
* **Returns:** None (saves file and prints status).

### `transcribe_audio(file_path: str)`

Transcribes audio content in a `.wav` file into text using Google's speech recognition engine.

* **Parameters:**

  * `file_path`: Path to the WAV file.
* **Returns:** Transcribed string (or `None` on failure).

## ⚠️ Limitations

* Requires internet connection for speech recognition (Google API).
* Only supports `.wav` format for audio input.
* Basic error handling for failed API calls and unintelligible speech.

## Future Improvements

* Support for other audio formats (e.g., MP3).
* Offline transcription via models like Vosk or Whisper.
* GUI interface or command-line arguments for ease of use.

## 📄 License

MIT License. See [LICENSE](LICENSE) file for details.
