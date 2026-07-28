# AI Voice Assistant

## Overview

This project is a simple AI Voice Assistant developed in Python. It records the user's voice, converts speech into text using Whisper, sends the text to Cohere AI to generate a response, and converts the response back into speech using Google Text-to-Speech (gTTS).

---

## Features

- 🎤 Voice recording from the microphone
- 📝 Speech-to-Text using Whisper
- 🤖 AI-generated responses using Cohere
- 🔊 Text-to-Speech using gTTS
- 🌍 Supports Arabic and English
- 💬 Interactive voice conversation

---

## Technologies Used

- Python
- OpenAI Whisper
- Cohere API
- Google Text-to-Speech (gTTS)
- sounddevice
- scipy
- python-dotenv
- playsound

---

## Project Structure

```text
VoiceAssistant-AI/
│── main.py
│── requirements.txt
│── .env.example
└── Ai1 - Trim.mp4
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/VoiceAssistant-AI.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Cohere API key:

```text
COHERE_API_KEY=YOUR_API_KEY
```

---

## Usage

Run the project:

```bash
python main.py
```

Then:

1. Speak into the microphone.
2. Your speech is converted into text.
3. Cohere generates an AI response.
4. The response is converted into speech and played back.

---

## Demo

A demonstration video is included in this repository:

**Ai1 - Trim.mp4**

---

## Author

**Ghala Alsufyani**
