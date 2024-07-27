import RPi.GPIO as GPIO
import time
import os
import random
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

audio_folder = "audio"

audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav') or f.endswith('.mp3')]

last_played = None

def play_random_audio():
    global last_played
    if len(audio_files) > 1:
        available_files = [f for f in audio_files if f != last_played]
        random_file = random.choice(available_files)
    elif audio_files:
        random_file = audio_files[0]
    else:
        return None
    
    last_played = random_file
    full_path = os.path.join(audio_folder, random_file)
    return subprocess.Popen(["play", "-q", full_path, "-t", "alsa"])

try:
    print("Press the big red button to play a random audio file.")
    player = None
    while True:
        if GPIO.input(26) == GPIO.LOW and player is None:
            print("Button pressed, starting playback...")
            time.sleep(0.8)
            player = play_random_audio()
            while GPIO.input(26) == GPIO.LOW:
                time.sleep(0.1)
            
            if player:
                player.terminate()
                player = None
            print("Button released, playback stopped.")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    if player:
        player.terminate()
    GPIO.cleanup()
