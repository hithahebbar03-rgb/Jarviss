import speech_recognition as sr
import subprocess
import time

# Targeted to your live development script
JARVIS_SCRIPT_PATH = r"C:\Users\A1\OneDrive\Desktop\Mark-XXXIX-main\main.py"

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("[WAKE WORD ENGINE] Calibrating microphone for ambient noise...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)

    print("[WAKE WORD ENGINE] Online. Listening for 'Jarvis'...")

    # Continuous loop monitoring the microphone in 3-second intervals
    while True:
        with microphone as source:
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
                command = recognizer.recognize_google(audio).lower()
                
                if "jarvis" in command:
                    print("[WAKE WORD ENGINE] Protocol recognized. Booting MARK XXXIX...")
                    
                    # Rerouted to execute the raw Python file
                    subprocess.Popen(["pythonw", JARVIS_SCRIPT_PATH])
                    
                    # 15-second cooldown to prevent infinite application loops
                    print("[WAKE WORD ENGINE] System launched. Entering 15-second cooldown.")
                    time.sleep(15)
                    print("[WAKE WORD ENGINE] Cooldown complete. Listening...")

            except sr.WaitTimeoutError:
                pass # Normal behavior, nobody is speaking
            except sr.UnknownValueError:
                pass # Normal behavior, ambient noise not recognized as speech
            except sr.RequestError:
                print("[WAKE WORD ENGINE] Critical Error: Unable to reach recognition servers.")
            except Exception as e:
                print(f"[WAKE WORD ENGINE] Unexpected Error: {e}")

if __name__ == "__main__":
    listen_for_wake_word()