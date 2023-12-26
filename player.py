import os
import pygame
from pydub import AudioSegment
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Constants
NUM_CHANNELS = 6
FILE_PATTERN = "out_{i}.wav"

class AudioPlayer:
    def __init__(self, directory: str):
        """Initializes the audio player with the given directory."""
        pygame.mixer.init()  
        self.directory = directory
        self.channel_files = [FILE_PATTERN.format(i=i) for i in range(1, NUM_CHANNELS + 1)]  
        self.observer = Observer()
        self.channels = [pygame.mixer.Channel(i) for i in range(NUM_CHANNELS)]  

    def start(self):
        """Starts the file observer."""
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_modified
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_file_modified(self, event):
        """Handles file modification events."""
        for channel in range(1, NUM_CHANNELS + 1):  
            if event.src_path.endswith(FILE_PATTERN.format(i=channel)):
                logging.info(f"File modified: {event.src_path}")
                self.stop_channel(channel) 

    def play_channel(self, channel: int, gain: int = 10):
        """Plays the audio on the given channel with the specified gain."""
        if 1 <= channel <= NUM_CHANNELS:
            self.stop_channel(channel)
            self.play_audio(FILE_PATTERN.format(i=channel), channel, gain)
        else:
            logging.error(f"Invalid channel number: {channel}")

    def play_audio(self, filename: str, channel: int, gain: int = 0):
        """Plays the given audio file on the specified channel with the given gain."""
        filepath = os.path.join(self.directory, filename)
        amplified_filepath = os.path.join(self.directory, f"amplified_{filename}")
        if os.path.exists(filepath):
            if (not os.path.exists(amplified_filepath) or
                os.path.getmtime(filepath) > os.path.getmtime(amplified_filepath)):
                try:
                    audio = AudioSegment.from_wav(filepath)
                    amplified_audio = audio.apply_gain(gain)
                    amplified_audio.export(amplified_filepath, format="wav")
                except Exception as e:
                    logging.error(f"Error processing audio file {filepath}: {e}")
            sound = pygame.mixer.Sound(amplified_filepath)
            self.channels[channel - 1].play(sound)
        else:
            logging.error(f"File not found: {filepath}")

    def play(self, filepath: str):
        """Plays the given audio file."""
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def stop_channel(self, channel: int): 
        """Stops the audio on the given channel."""
        if 1 <= channel <= NUM_CHANNELS:
            self.channels[channel - 1].stop()
        else:
            logging.error(f"Invalid channel number: {channel}")

    def set_volume(self, channel: int, volume: float):
        """Sets the volume for the given channel."""
        if 1 <= channel <= NUM_CHANNELS and 0.0 <= volume <= 1.0:
            self.channels[channel - 1].set_volume(volume)
        else:
            logging.error(f"Invalid channel number or volume level: {channel}, {volume}")      

player = AudioPlayer(os.path.join(os.path.dirname(__file__), 'output'))
player.start()
