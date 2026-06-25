import sys
import asyncio
import tempfile

import pyperclip
import edge_tts
import pygame

from PyQt6.QtWidgets import QApplication, QPushButton, QWidget
from PyQt6.QtCore import Qt, QPoint


class FloatingButton(QWidget):
    def __init__(self):
        super().__init__()

        pygame.mixer.init()

        self.setGeometry(100, 100, 80, 80)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.button = QPushButton("🔊", self)
        self.button.setGeometry(0, 0, 80, 80)
        self.button.clicked.connect(self.read_clipboard)

        self.drag_position = QPoint()

    async def generate_speech(self, text):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )
        temp_file.close()

        communicate = edge_tts.Communicate(
            text,
            voice="en-US-JennyNeural"
        )

        await communicate.save(temp_file.name)

        return temp_file.name

    def read_clipboard(self):
        text = pyperclip.paste()

        if not text.strip():
            print("Clipboard is empty.")
            return

        print("Reading:", text[:100])

        # Stop current playback if any
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        # Generate a new audio file
        audio_file = asyncio.run(self.generate_speech(text))

        # Play it
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(
                event.globalPosition().toPoint()
                - self.drag_position
            )


app = QApplication(sys.argv)

window = FloatingButton()
window.show()

sys.exit(app.exec())