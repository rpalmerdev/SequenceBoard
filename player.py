##Program for handling audio playback
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import threading
import pygame

class AudioPlayer:
    def __init__(self, directory):
        self.directory = directory
        self.channel_files = [f"out_{i}.wav" for i in range(1, 7)]  # Channel files
        self.observer = Observer()
        self.processes = {}
        pygame.mixer.init()

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_modified
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_file_modified(self, event):
        for channel in range(1, 7):  # Check for all channels
            if event.src_path.endswith(f"out_{channel}.wav"):
                print(f"File modified: {event.src_path}")

    def play_channel(self, channel):
        # Check if the channel number is valid
        if 1 <= channel <= 6:
            # Stop the current audio for the channel if it's playing
            self.stop_channel(channel)
            # Play the corresponding audio file
            self.play_audio(f"out_{channel}.wav", channel)
        else:
            print(f"Invalid channel number: {channel}")

    def play_audio(self, filename, channel):
        filepath = os.path.join(self.directory, filename)
        if os.path.exists(filepath):
            self.processes[channel] = threading.Thread(target=self.play, args=(filepath,))
            self.processes[channel].start()
        else:
            print(f"File not found: {filepath}")

    def play(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def stop_channel(self, channel):  # Modify this method
        if channel in self.processes:
            pygame.mixer.music.stop()
            self.processes[channel].join()
            del self.processes[channel]

# Use the class
player = AudioPlayer(os.path.join(os.path.dirname(__file__), 'output'))
player.start()
