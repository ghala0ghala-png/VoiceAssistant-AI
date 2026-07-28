import os
import whisper
import cohere
from gtts import gTTS
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv

# تحميل مفتاح Cohere
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    print("API Key not found!")
    exit()

# الاتصال بـ Cohere
co = cohere.Client(api_key)

# تحميل نموذج Whisper
print("Loading Whisper...")
model = whisper.load_model("base")

# محرك تحويل النص إلى صوت


import os
from gtts import gTTS
from playsound import playsound

def speak(text):
    print("\nAI:", text)

    filename = "reply.mp3"

    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            pass

    if any('\u0600' <= c <= '\u06FF' for c in text):
      tts= gTTS(text=text, lang="ar")
    else:
     tts = gTTS(text=text, lang="en")
    tts.save(filename)

    playsound(filename)


def record_audio(filename="input.wav", duration=5, fs=16000):
    print("\n🎤 Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    write(filename, fs, recording)
    print("Recording finished.")


print("====================================")
print(" Voice Assistant Started ")
print(" قل شيئًا وسيتم تسجيله لمدة 5 ثوانٍ")
print(" اضغط Ctrl + C للخروج")
print("====================================")

while True:
    try:
        # تسجيل الصوت
        record_audio()

        # تحويل الصوت إلى نص
        result = model.transcribe(
    "input.wav",
    task="transcribe"
)
        user_text = result["text"].strip()

        if user_text == "":
            print("لم يتم التعرف على أي كلام.")
            continue

        print("\nYou:", user_text)
        # إرسال إلى Cohere
        response = co.chat(
            model="command-a-03-2025",
            message=user_text,
            preamble="Answer in one or two short sentences only."
        )

        reply = response.text

        # تقصير الرد إذا كان طويلًا
        sentences = reply.split(".")
        if len(sentences) > 2:
            reply = ".".join(sentences[:2]) + "."

        # نطق الرد
        speak(reply)

    except KeyboardInterrupt:
        print("\nGoodbye!")
        break

    except Exception as e:
        print("Error:", e)