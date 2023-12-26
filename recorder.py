import soundfile as sf
import pyaudiowpatch as pyaudio
import numpy as np
import os
import logging

# Constants
NUM_CHANNELS = 6

class Recorder:
    def __init__(self, buffer_size=512):
        """Initializes the recorder with empty data for each channel."""
        self.data = {i: [] for i in range(1, NUM_CHANNELS + 1)}
        self.output_channel = 1  
        self.sample_rate = None
        self.buffer_size = buffer_size
        self.stream = None

    def record_audio(self):
        """Records audio from the default output device."""
        p = pyaudio.PyAudio()

        # Get default WASAPI info
        wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)

        # Get default WASAPI speakers
        default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])
        self.sample_rate = int(default_speakers["defaultSampleRate"]) 

        if not default_speakers["isLoopbackDevice"]:
            for loopback in p.get_loopback_device_info_generator():
                if default_speakers["name"] in loopback["name"]:
                    default_speakers = loopback
                    break
            else:
                logging.error(
                    "Default loopback output device not found.\n\nRun `python -m pyaudiowpatch` to check available devices.\nExiting...\n")
                raise RuntimeError("Default loopback output device not found")

        logging.info(f"Recording from: ({default_speakers['index']}){default_speakers['name']}")

        def callback(in_data: bytes, frame_count: int, time_info, status) -> tuple:
            """Handles new audio data by appending it to the current output channel's data."""
            data = np.frombuffer(in_data, dtype=np.int16)
            data = data.reshape(-1, 2)  # Reshape to a 2-D array (stereo)
            self.data[self.output_channel].append(data)
            return (in_data, pyaudio.paContinue)

        # Open the stream
        self.stream = p.open(format=pyaudio.paInt16,
                             channels=2,
                             rate=self.sample_rate,
                             input=True,
                             frames_per_buffer=self.buffer_size,
                             input_device_index=default_speakers['index'],
                             stream_callback=callback)

    def start_recording(self):
        logging.info(f"Recording started for channel {self.output_channel}...")
        self.record_audio()
        self.stream.start_stream()

    def stop_recording(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            logging.info(f"Recording stopped for channel {self.output_channel}.")
            output_filename = f"out_{self.output_channel}.wav"
            output_path = os.path.join('output', output_filename)
            sf.write(output_path, np.concatenate(self.data[self.output_channel]), self.sample_rate,
                     'PCM_16')  # Write in stereo
            self.data[self.output_channel] = []

    def set_output_channel(self, channel):
        self.output_channel = channel


if not os.path.exists('output'):
    os.makedirs('output')

recorder = Recorder()


