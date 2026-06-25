import pyttsx3
import pyperclip

text = pyperclip.paste()

if not text.strip():
    print("Clipboard is empty.")
else:
    print("Reading:", text[:100])

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()