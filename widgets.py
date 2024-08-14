from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QGridLayout, QFileDialog
import threading
from gtts import gTTS
from playsound import playsound
import tempfile
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Creating Window
        self.setWindowTitle("Text To Speech")
        self.resize(400, 300)

        # Initialising Widgets
        self.entry = QLineEdit()
        self.play_button = QPushButton("Play")
        self.download_button = QPushButton("Download")

        # Button Actions
        self.play_button.clicked.connect(self.play)
        self.download_button.clicked.connect(self.download)

        # Initialising Layout
        layout = QGridLayout()
        layout.addWidget(self.entry, 0, 1)
        layout.addWidget(self.download_button, 0, 2)
        layout.addWidget(self.play_button, 1, 0, 1, 3)

        self.setLayout(layout)

    # Function to play the text to speech audio
    def play(self):
        def play_thread():
            text = self.entry.text()

            try:
                tts = gTTS(text)
                temp_file = tempfile.NamedTemporaryFile(prefix="mp3", delete=False)

                tts.save(temp_file.name)
                temp_file.close()

                file_path = temp_file.name
                playsound(file_path)
                os.remove(file_path)
            except AssertionError:
                pass

        thread = threading.Thread(target=play_thread)
        thread.start()

    # Function to download text to speech audio
    def download(self):
        file_dir = QFileDialog.getExistingDirectory()
        text = self.entry.text()
        tts = gTTS(text)
        temp_file = tempfile.NamedTemporaryFile(prefix="TTS", delete=False, dir=file_dir)

        tts.save(f"{temp_file.name}.mp3")
        temp_file.close()
        file_path = temp_file.name
        os.remove(file_path)
