##Program for handling audio playback
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pygame

class AudioPlayer:
    def __init__(self, directory):
        pygame.mixer.init()  # Initialize the mixer module first
        self.directory = directory
        self.channel_files = [f"out_{i}.wav" for i in range(1, 7)]  # Channel files
        self.observer = Observer()
        self.channels = [pygame.mixer.Channel(i) for i in range(6)]  # Now you can create the Channel objects

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_modified
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_file_modified(self, event):
        for channel in range(1, 7):  # Check for all channels
            if event.src_path.endswith(f"out_{channel}.wav"):
                print(f"File modified: {event.src_path}")
                self.stop_channel(channel)  # Stop the audio for the modified channel
                

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
            sound = pygame.mixer.Sound(filepath)  # Create a Sound object
            self.channels[channel - 1].play(sound)  # Play the sound on the corresponding channel
        else:
            print(f"File not found: {filepath}")

    def play(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def stop_channel(self, channel):  # Modify this method
        if 1 <= channel <= 6:
            self.channels[channel - 1].stop()  # Stop the sound on the corresponding channel

# Use the class
player = AudioPlayer(os.path.join(os.path.dirname(__file__), 'output'))
player.start()
