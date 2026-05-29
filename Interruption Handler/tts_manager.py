import pyttsx3
import threading

class TTSManager:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 160)

        self.tts_active = False

    def speak(self, text):

        def run():

            self.tts_active = True

            print("\n[TTS STARTED]\n")

            self.engine.say(text)

            self.engine.runAndWait()

            self.tts_active = False

            print("\n[TTS FINISHED]\n")

        threading.Thread(target=run, daemon=True).start()

    def stop(self):

        if self.tts_active:

            self.engine.stop()

            self.tts_active = False

            print("\n[TTS STOPPED]\n")

    def is_speaking(self):

        return self.tts_active