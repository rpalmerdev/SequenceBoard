# 🎵SequenceBoard🎵

##  ![warning](https://github.com/rpalmerdev/SequenceBoard/assets/52892010/45d45d54-2f2e-4262-bd82-98765dda9627) 
## **(UNDER CONSTRUCTION)** 


![waveform](https://github.com/rpalmerdev/SequenceBoard/assets/52892010/275a7046-e01f-452b-b8a6-55c0a211139a)
Baby's first coding project, written in Python (3.11.5) with ~~*a little*~~ ***way*** too much help from GitHub Copilot. 😅
Aims to be a six-channel desktop loopback recorder with built-in sequencer. For making meme-y beats with whatever is playing on your desktop.

## **✅Currently working:** 
Loopback recording and playback on **Windows** to six channels in the GUI with per-channel volume control. Basically a soundboard.
*Note: currently working on **my** Windows desktop with a 13900k. Have noticed some playback issues on my laptop and am investigating.*

## **❌Currently working on:** 
Audio trimming with visible waveforms, real-time gain meters, effects processing, sequencer, UI improvements, general performance and reliability, Linux/Mac compatiblity.

## **🩼Dependencies:**
[PyAudioWPatch](https://github.com/s0d3s/PyAudioWPatch/)
[pygame](https://github.com/pygame/pygame)
[pyside6](https://pypi.org/project/PySide6/)
[pydub](https://github.com/jiaaro/pydub)
[soundfile](https://pypi.org/project/soundfile/)
[watchdog](https://pypi.org/project/watchdog/)
[numpy](https://github.com/numpy/numpy)

## **💸License:** 
[GNU GPL v3](https://github.com/rpalmerdev/SequenceBoard/blob/main/LICENSE)

## 🔥Crappy Showcase Video (loud music)

https://github.com/rpalmerdev/SequenceBoard/assets/52892010/0de317cf-59e3-48f9-9b0a-49d44001f367

## ❗Installation

1. **If you don't have it, install Python:**
   - Download and install Python 3.11.5 from [python.org](https://www.python.org/downloads/release/python-3115)
   - Otherwise, skip to step 2.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/rpalmerdev/SequenceBoard.git
   cd SequenceBoard

3. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment:**
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

5. **Install Python 3.11.5 within the Virtual Environment:**
    ```bash
    pip install python==3.11.5
    ```

6. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt 
    ```
## ❗Usage

1. **Open a terminal in the project folder, or:**
   ```bash
   cd SequenceBoard
   ```
2. **Activate the Virtual Environment:**
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
3. **Run main.py**
   - On Windows:
       ```bash
       python .\main.py
       ```

##
*SequenceBoard: A soundboard/sequencer for desktop audio loopback. 
    Copyright (C) 2023  Bobby Palmer*

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

