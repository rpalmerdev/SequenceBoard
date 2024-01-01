import os
import pygame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import threading
from PySide6.QtCore import QObject, Signal
import soundfile as sf

NUM_CHANNELS = 6
FILE_PATTERN = "out_{i}.wav"

class AudioPlayer(QObject):
    audio_loaded = Signal(object)
    def __init__(self, directory: str):
        super().__init__() 
        pygame.mixer.pre_init(buffer=4096)
        pygame.mixer.init() 
        self.directory = directory
        self.channel_files = [FILE_PATTERN.format(i=i) for i in range(1, NUM_CHANNELS + 1)]  
        self.observer = Observer()
        self.channels = {i: pygame.mixer.Channel(i) for i in range(NUM_CHANNELS)}  
        
    def start(self): #observer
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_modified
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_file_modified(self, event):
        for channel in range(1, NUM_CHANNELS + 1):  
            if event.src_path.endswith(FILE_PATTERN.format(i=channel)):
                logging.info(f"File modified: {event.src_path}")
                self.stop_channel(channel) 

    def play_channel(self, channel: int): 
        if 1 <= channel <= NUM_CHANNELS:
            self.stop_channel(channel)
            threading.Thread(target=self.play_audio, args=(FILE_PATTERN.format(i=channel), channel)).start()  
        else:
            logging.error(f"Invalid channel number: {channel}")

    def play_audio(self, filename: str, channel: int):
        filepath = os.path.join(self.directory, filename)
        if os.path.exists(filepath):
            try:
                sound = pygame.mixer.Sound(filepath)
                self.channels[channel - 1].play(sound)
                data, _ = sf.read(filepath)  
                self.audio_loaded.emit(data) 
            except pygame.error as e:
                logging.error(f"Error playing audio file {filepath}: {e}")
        else:
            logging.error(f"File not found: {filepath}")

    def play(self, filepath: str):
        try:
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()
        except pygame.error as e:
            logging.error(f"Error playing audio file {filepath}: {e}")

    def stop_channel(self, channel: int): 
        if 1 <= channel <= NUM_CHANNELS:
            self.channels[channel - 1].stop()
        else:
            logging.error(f"Invalid channel number: {channel}")
        
    def set_volume(self, channel: int, volume: float):
        if 1 <= channel <= NUM_CHANNELS and 0.0 <= volume <= 1.0:
            self.channels[channel - 1].set_volume(volume)
        else:
            logging.error(f"Invalid channel number or volume level: {channel}, {volume}")      

player = AudioPlayer(os.path.join(os.path.dirname(__file__), 'output'))
player.start()
        


        
        

        
