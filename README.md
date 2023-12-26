# SequenceBoard

**((UNDER CONSTRUCTION))**

First time coding project, written in Python (3.11.5) with a little too much help from GitHub Co-pilot. 

Aims to be a six-channel desktop audio loopback recorder with built-in sequencer. For making meme-y beats with whatever is playing on your desktop.

**Currently working:** Loopback recording and playback on Windows to 6 channels in the GUI. Basically a soundboard currently.

**Currently working on:** Audio trimming with visible waveforms, real-time gain meters, effects processing, sequencer. Probably going to have to figure out threading. 

**Dependencies:**
Patched PyAudio library called [PyAudioWPatch](https://github.com/s0d3s/PyAudioWPatch/) for loopback functionality on Windows.
[pygame](https://github.com/pygame/pygame)
[pyside6](https://pypi.org/project/PySide6/)
[pydub](https://github.com/jiaaro/pydub)
[soundfile](https://pypi.org/project/soundfile/)
[watchdog](https://pypi.org/project/watchdog/)
[numpy](https://github.com/numpy/numpy)
