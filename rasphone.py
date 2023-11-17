import time
import board
import RPi.GPIO as GPIO
import os
import adafruit_matrixkeypad
import digitalio
import random
import pygame.mixer as mixer
import pygame

PICKUP_BUTTON = 23
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(PICKUP_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init()

audio_files = {
    "accueil": "audio_files/accueil.wav",
    "menu": "audio_files/menu.wav",
    "prerecord": "audio_files/prerecord.wav",
    "beep": "audio_files/beep.wav",
    "prerandom": "audio_files/prerandom.wav",
    0: "audio_files/audio0.wav",
    1: "audio_files/audio1.wav",
    2: "audio_files/audio2.wav",
    3: "audio_files/audio3.wav",
    11: "audio_files/audio11.wav",
    12: "audio_files/audio12.wav",
    13: "audio_files/audio13.wav",
}

record_directory = "record"

def play_audio(file_number):
    if file_number in audio_files:
        audio_file = audio_files[file_number]
        sound = mixer.Sound(audio_file)
        sound.play()

def start_recording():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    record_filename = os.path.join(record_directory, f"{timestamp}.wav")
    os.system(f"arecord -d 60 -f cd {record_filename}")
    
def play_random():
    recordings = [os.path.join(record_directory, file) for file in os.listdir(record_directory) if file.endswith(".wav")]
    if recordings:
        random_recording = random.choice(recordings)
        sound = mixer.Sound(random_recording)
        sound.play()

def pickup_button(channel):
    global current_state
    if GPIO.input(PICKUP_BUTTON) == GPIO.LOW:
        print('working')
        menu = 'start'
        while GPIO.input(PICKUP_BUTTON) == GPIO.LOW:
            keys = keypad.pressed_keys
            #play_audio('accueil')
            #play_audio('menu')
            if 0 in keys:
                mixer.stop()
                play_audio('menu')
                menu = 'start'
                print(menu)
            elif menu == 'start' and 1 in keys:
                mixer.stop()
                play_audio(1)
                menu = '1'
                print(menu)
            elif menu == '1' and 1 in keys:
                mixer.stop()
                play_audio(11)
                menu = '11'
                print(menu)
            elif menu == '1' and 2 in keys:
                mixer.stop()
                play_audio('menu')
                menu = 'start'
                print(menu)
            elif 2 in keys and menu == 'start':
                mixer.stop()
                menu = '2'
                print(menu)
                start_recording()
            elif menu == 'start' and 3 in keys:
                mixer.stop()
                menu = 'random'
                print(menu)
                play_random()
            elif 9 in keys:
                menu = 'shutdown-2'
                print(menu)
            elif menu == 'shutdown-2' and 8 in keys:
                menu = 'shutdown-1'
                print(menu)
            elif menu == 'shutdown-1' and 7 in keys:
                menu = 'shutdown now'
                print(menu)
                os.system("shutdown -h now")
            time.sleep(0.3)
    else:
        print('sleeping')
        mixer.stop()
        os.system("pkill -15 arecord")
    time.sleep(0.1)

cols = [digitalio.DigitalInOut(x) for x in (board.D16, board.D26, board.D6)]
rows = [digitalio.DigitalInOut(x) for x in (board.D5, board.D22, board.D27, board.D17)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

GPIO.add_event_detect(PICKUP_BUTTON, GPIO.BOTH, callback=pickup_button)

try:
    print('Ready')
    input()
    time.sleep(0.1)

except KeyboardInterrupt:
    pass
    GPIO.cleanup()

GPIO.cleanup()
