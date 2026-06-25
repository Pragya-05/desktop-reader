import pyperclip
import pyttsx3

text = pyperclip.paste()

print("Reading:", text)

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()