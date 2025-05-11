import pyttsx3
import speech_recognition as sr

def text_to_speech(text, filename):
    """Converts text to speech and saves as a WAV file."""
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Audio saved as {filename}")

def transcribe_audio(file_path):
    """Transcribes speech from a WAV file to text."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        print("Listening to the audio...")
        audio_data = recognizer.record(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio_data)
        print("Transcription:\n", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"API request error: {e}")

if __name__ == "__main__":
    # Step 1: Generate audio from text
    input_text = "Hello, my name is Alex and I love programming."
    audio_path = "example.wav"
    text_to_speech(input_text, audio_path)

    # Step 2: Transcribe the generated audio
    transcribe_audio(audio_path)