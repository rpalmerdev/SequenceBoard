##Program for handling audio playback
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pygame
from pydub import AudioSegment

class AudioPlayer:
    def __init__(self, directory):
        pygame.mixer.init()  
        self.directory = directory
        self.channel_files = [f"out_{i}.wav" for i in range(1, 7)]  
        self.observer = Observer()
        self.channels = [pygame.mixer.Channel(i) for i in range(6)]  

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_modified
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()

    def on_file_modified(self, event):
        for channel in range(1, 7):  
            if event.src_path.endswith(f"out_{channel}.wav"):
                print(f"File modified: {event.src_path}")
                self.stop_channel(channel) 
                
    def play_channel(self, channel, gain=10):
        # Check if the channel number is valid
        if 1 <= channel <= 6:
            # Stop the current audio for the channel if it's playing
            self.stop_channel(channel)
            # Play the corresponding audio file with the specified gain
            self.play_audio(f"out_{channel}.wav", channel, gain)
        else:
            print(f"Invalid channel number: {channel}")

    def play_audio(self, filename, channel, gain=0):
        filepath = os.path.join(self.directory, filename)
        amplified_filepath = os.path.join(self.directory, f"amplified_{filename}")
        if os.path.exists(filepath):
            # Check if the amplified file exists and is up-to-date
            if (not os.path.exists(amplified_filepath) or
                os.path.getmtime(filepath) > os.path.getmtime(amplified_filepath)):
                # Load the audio file with pydub
                audio = AudioSegment.from_wav(filepath)
                # Amplify the audio
                amplified_audio = audio.apply_gain(gain)
                # Export the amplified audio to a file
                amplified_audio.export(amplified_filepath, format="wav")
            # Load the amplified audio with pygame
            sound = pygame.mixer.Sound(amplified_filepath)
            self.channels[channel - 1].play(sound)
        else:
            print(f"File not found: {filepath}")

    def play(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def stop_channel(self, channel): 
        if 1 <= channel <= 6:
            self.channels[channel - 1].stop()
            
    def set_volume(self, channel, volume):
        # Check if the channel number and volume level are valid
        if 1 <= channel <= 6 and 0.0 <= volume <= 1.0:
            self.channels[channel - 1].set_volume(volume)
        else:
            print(f"Invalid channel number or volume level: {channel}, {volume}")      


player = AudioPlayer(os.path.join(os.path.dirname(__file__), 'output'))
player.start()

