# Interruption Handling System

## Overview

This project implements a real-time interruption handling system for voice-based AI assistants.

The system continuously monitors microphone input while Text-to-Speech (TTS) is active. If the user interrupts the assistant by speaking during TTS playback, the system immediately pauses the speech output and switches into listening mode.

---

# Objective

* Detect overlapping speech
* Handle user interruptions during TTS playback
* Maintain smooth conversational flow
* Reduce false positives
* Provide low-latency interruption handling

---

# Features

* Real-time microphone monitoring
* Voice interruption detection
* Automatic TTS stopping
* Listening mode activation
* Cooldown handling for rapid interruptions
* Modular and integration-ready architecture

---

# Project Structure

```text
interruption_handler/
│
├── main.py
├── interruption_manager.py
├── tts_manager.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

* Python
* NumPy
* SoundDevice
* pyttsx3

---

# Installation

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
cd interruption_handler
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python main.py
```

---

# Demo Flow

1. System starts TTS playback
2. User interrupts while TTS is active
3. Interruption is detected in real-time
4. TTS playback stops immediately
5. System switches to listening mode

---

# Example Output

```json
{
    "interruption": true,
    "action": "pause_tts"
}
```

---

# Edge Cases Handled

* False positives using threshold-based detection
* Rapid interruptions using cooldown logic
* Low-latency switching between states

---

# Future Improvements

* Advanced Voice Activity Detection (VAD)
* Echo cancellation
* Speech-to-Text integration
* Speaker identification
* Noise suppression

---

# Author

Internship Project Submission
Phase 4 — Interruption Handling System
