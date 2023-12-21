import soundcard as sc
import soundfile as sf
import numpy as np
import threading
import os
from pydub import AudioSegment


samplerate = 48000
buffer_size = 128
gain = 10  # dB

class Recorder:
    def __init__(self):
        self.data = []
        self.recording = False
        self.recording_counter = 0
        self.output_channel = 0

    def record_audio(self):
        try:
            with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=samplerate) as mic:
                while True:
                    chunk = mic.record(numframes=samplerate//buffer_size)
                    if self.recording:
                        self.data.append(chunk)
                    elif self.data:
                        print(f"Recording stopped for channel {self.output_channel}.")
                        output_filename = f"out_{self.output_channel}.wav"
                        output_path = os.path.join('recordings', output_filename)
                        sf.write(output_path, np.concatenate(self.data), samplerate=samplerate)
                        self.amplify_audio(output_path, output_path, gain)  # Amplify the audio by 'x' dB
                        self.data.clear()
        except Exception as e:
            print(f"An error occurred during recording: {e}")

    def start_recording(self):
        print(f"Recording started for channel {self.output_channel}...")
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def set_output_channel(self, channel):
        self.output_channel = channel

    def amplify_audio(self, input_file, output_file, amplification_factor):
        audio = AudioSegment.from_file(input_file)
        amplified_audio = audio + amplification_factor
        amplified_audio.export(output_file, format='wav')

if not os.path.exists('recordings'):
    os.makedirs('recordings')

# Create a recorder
recorder = Recorder()

# Start a new thread for the recorder
threading.Thread(target=recorder.record_audio, daemon=True).start()

# Handle user input
while True:
    command = input("Enter command (start/stop/set_channel/exit) and channel number (0-5): ")
    command_parts = command.split()
    if command_parts[0] == 'start':
        recorder.start_recording()
    elif command_parts[0] == 'stop':
        recorder.stop_recording()
    elif command_parts[0] == 'set_channel':
        recorder.set_output_channel(int(command_parts[1]))
    elif command_parts[0] == 'exit':
        print("Exiting...")
        break
    else:
        print("Invalid command. Please enter 'start', 'stop', 'set_channel', or 'exit'.")