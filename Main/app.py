import pygame
from tkinter import *
from tkinter import filedialog
import os

def stop_song():
    pygame.mixer.music.stop()

class MP3Player:
    def __init__(self, root):
        self.file_path = None
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("300x250")
        
        pygame.mixer.init()
        
        self.track = StringVar()
        self.error_message = StringVar()
        
        self.track_label = Label(root, textvariable=self.track)
        self.track_label.pack()
        
        self.play_button = Button(root, text="Play", command=self.play_song)
        self.play_button.pack()
        
        self.stop_button = Button(root, text="Stop", command=stop_song)
        self.stop_button.pack()
        
        self.load_button = Button(root, text="Load", command=self.load_song)
        self.load_button.pack()

        self.error_label = Label(root, textvariable=self.error_message, fg="red")
        self.error_label.pack()
        
    def load_song(self):
        self.error_message.set("")
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.track.set(os.path.basename(self.file_path))
            print(f"Loaded file: {self.file_path}")
    
    def play_song(self):
        if self.file_path:
            try:
                pygame.mixer.music.load(self.file_path)
                pygame.mixer.music.play()
                print(f"Playing file: {self.file_path}")
            except pygame.error as e:
                self.error_message.set("Unsupported file format!")
                print(f"Could not load file: {e}")
        else:
            self.error_message.set("No file loaded to play")
            print("No file loaded to play")

if __name__ == "__main__":
    root = Tk()
    app = MP3Player(root)
    root.mainloop()