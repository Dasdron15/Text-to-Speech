import tkinter as tk
from tkinter import filedialog
import threading
from gtts import gTTS
import pygame
import tempfile
import os

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech")
        self.root.geometry("400x300")

        self.entry = tk.Entry(root, width=40)
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.download_button = tk.Button(root, text="Download", command=self.download)

        self.entry.pack(pady=10)
        self.play_button.pack(pady=5)
        self.download_button.pack(pady=5)

    # Function to play the text to speech audio
    def play(self):
        def play_thread():
            pygame.mixer.init()
            text = self.entry.get()

            try:
                tts = gTTS(text)
                temp_file = tempfile.NamedTemporaryFile(prefix="mp3", delete=False)

                tts.save(temp_file.name)
                temp_file.close()

                file_path = temp_file.name
                sound = pygame.mixer.Sound(file_path)

                sound.play()
                
                os.remove(file_path)
            except Exception as e:
                print("Error: ", e)

        threading.Thread(target=play_thread, daemon=True).start()

    # Function to download text to speech audio
    def download(self):
        file_dir = filedialog.askdirectory()
        if not file_dir:
            return

        text = self.entry.get().strip()
        if not text:
            return

        tts = gTTS(text)

        file_name = "_".join(text.split())[:20]
        file_path = os.path.join(file_dir, f"{file_name}.mp3")

        tts.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
