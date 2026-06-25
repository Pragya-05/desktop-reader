import keyboard
import pyperclip
import pyttsx3
import time

engine = pyttsx3.init()

def read_selected_text():
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.3)

    text = pyperclip.paste()

    if text.strip():
        print("Reading...")
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text selected.")

print("Desktop Reader Running...")
print("Press Ctrl + Shift + R to read selected text.")
print("Press ESC to quit.")

keyboard.add_hotkey('ctrl+shift+r', read_selected_text)

keyboard.wait('esc')