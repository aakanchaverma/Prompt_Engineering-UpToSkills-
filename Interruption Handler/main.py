import threading
import time

from tts_manager import TTSManager
from interruption_manager import InterruptionManager

def main():

    print("\n===================================")
    print("REAL-TIME INTERRUPTION SYSTEM")
    print("===================================\n")

    tts = TTSManager()

    interruption_manager = InterruptionManager(tts)

    # Start interruption monitoring

    listener_thread = threading.Thread(
        target=interruption_manager.start,
        daemon=True
    )

    listener_thread.start()

    time.sleep(2)

    # Start TTS

    tts.speak(
        """
        Hello user.
        This is a real-time interruption handling demo.
        Please interrupt me while I am speaking.
        """
    )

    # Keep program alive

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()