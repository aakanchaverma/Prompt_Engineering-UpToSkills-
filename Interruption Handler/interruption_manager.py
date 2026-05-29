import sounddevice as sd
import numpy as np
import time


class InterruptionManager:

    def __init__(self, tts_manager):

        self.tts_manager = tts_manager

        self.volume_threshold = 0.005

        self.consecutive_frames = 0

        self.required_frames = 5

        self.last_interrupt_time = 0

        self.cooldown = 2.0

        self.running = False

        self.interrupted = False

    # ====================================
    # AUDIO CALLBACK
    # ====================================

    def audio_callback(self, indata, frames, time_info, status):

        if status:
            print(status)

        # Get microphone volume

        volume_norm = np.max(np.abs(indata))

        # Only print meaningful values

        if volume_norm > 0.01:
            print(f"Volume: {volume_norm:.5f}")

        # Detect interruption ONLY during TTS

        if (
            self.tts_manager.is_speaking()
            and not self.interrupted
        ):

            if volume_norm > self.volume_threshold:

                self.consecutive_frames += 1

                print(
                    f"[Possible Interruption] "
                    f"Frames = {self.consecutive_frames}"
                )

            else:

                self.consecutive_frames = 0

            current_time = time.time()

            # Trigger interruption

            if (
                self.consecutive_frames
                >= self.required_frames
                and current_time - self.last_interrupt_time
                > self.cooldown
            ):

                self.last_interrupt_time = current_time

                self.handle_interruption()

                self.consecutive_frames = 0

    # ====================================
    # INTERRUPTION HANDLER
    # ====================================

    def handle_interruption(self):

        self.interrupted = True

        print("\n========================")
        print("INTERRUPTION DETECTED")
        print("========================")

        output = {
            "interruption": True,
            "action": "pause_tts"
        }

        print(output)

        self.tts_manager.stop()

        print("\n[SWITCHED TO LISTENING MODE]\n")

        # Prevent retrigger loop

        time.sleep(2)

        self.consecutive_frames = 0

        self.interrupted = False

    # ====================================
    # START LISTENING
    # ====================================

    def start(self):

        self.running = True

        print("\n[INTERRUPTION MANAGER ACTIVE]\n")

        with sd.InputStream(
            callback=self.audio_callback,
            channels=1,
            samplerate=44100,
            blocksize=1024
        ):

            while self.running:
                time.sleep(0.1)

    # ====================================
    # STOP SYSTEM
    # ====================================

    def stop(self):

        self.running = False