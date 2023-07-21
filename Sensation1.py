import os
import cv2
import datetime
import requests
import psutil
import re
import json
import time
import threading
import nltk
from nltk.tokenize import word_tokenize
import sounddevice as sd
import pyttsx3
import geocoder
from vosk import Model, KaldiRecognizer
import queue
import navigation # Import the navigation.py file

#nltk.download('punkt')

# Loading the vosk model
model = Model("vosk-model-small-en-in-0.4")  # Replace "path/to/your/vosk/model" with the actual path to your Vosk language model or keep it in the same python file 

# Initialize the recognizer and the text-to-speech engine
engine = pyttsx3.init()

# Function to listen to the user's voice input
def listen():
    samplerate = 16000  # The sampling rate used by Vosk
    blocksize = 8000   # The blocksize used by Vosk

    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, channels=1, dtype="int16", callback=callback):
        print("Listening...")
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                try:
                    json_result = json.loads(result)
                    recognized_text = json_result["text"]
                    print("You said:", recognized_text)
                    return recognized_text
                except json.JSONDecodeError:
                    print("Failed to parse JSON:", result)
            else:
                print("Recognizing...")

# Function to clear memory in a separate thread
def clear_memory_thread():
    while True:
        process = psutil.Process(os.getpid())
        process.memory_info().rss  # Force memory update
        time.sleep(5)  # Wait for 5 seconds
        print("Memory cleared.")

# Function to speak the assistant's response
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    return f"The current time is {current_time}"

# Function to get the current date
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    return f"Today's date is {current_date}"

# Function to get the current day
def get_day():
    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    return f"Today is {current_day}"

# Function to run the navigation file
def get_location():
    return navigation.get_location()

# Function to take a picture and save it
def take_picture():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    camera.release()

    if return_value:
        folder_path = "C:/Users/User_name/Pictures/Clicked pictures"  # Replace with your Windows username
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Generate a unique file name using the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"picture_{timestamp}.jpg"
        file_path = os.path.join(folder_path, file_name)
        cv2.imwrite(file_path, image)

        return f"Picture taken and saved as {file_name} successfully!"
    else:
        return "Sorry, there was an error capturing the picture."

# Function to shut down the system
def shutdown_system(user_tokens=None):
    speak("Do you want to shut down the system?")
    response = listen()
    if response and "yes" in response.lower():
        os.system("shutdown /s /t 0")
        return "System is shutting down..."
    else:
        return "Okay, the system will not be shut down."

# Function to start navigation
def start_navigation():
    global navigation_running
    navigation_running = True
    speak("Navigation is now running.")

# Function to stop navigation
def stop_navigation():
    global navigation_running
    navigation_running = False
    speak("Navigation has been stopped.")

# Welcome message
speak("Welcome to Sensation! How can I assist you?")

# Variable to keep track of whether navigation is running
navigation_running = False

# A dictionary to map commands to functions
commands = {
    "time": get_time,
    "date": get_date,
    "day": get_day,
    "position": get_location,
    "location": get_location,
    "address": get_location,
    "where am i now": get_location,
    "navigation": start_navigation,
    "start navigation": start_navigation,
    "picture": take_picture,
    "photo": take_picture,
    "selfie": take_picture,
    "shot": take_picture,
    "shut": shutdown_system,
    "down": shutdown_system,
    "turn": shutdown_system,
    "off": shutdown_system,
    "stop": lambda user_tokens=None: "Goodbye! See you again.",
}

# Regular expression for matching specific commands preceded by the trigger word
trigger_word = "sensation"
navigation_stop_phrase = "stop navigation"
command_pattern = re.compile(
    rf"(?i)\b{trigger_word}\b.*\b(?:time|date|day|position|address|location|navigation|start navigation|picture|photo|selfie|shot|shut|down|turn|off|stop|city|state|country|street|{navigation_stop_phrase})\b"
)

# Thread for clearing memory
memory_clear_thread = threading.Thread(target=clear_memory_thread)
memory_clear_thread.daemon = True
memory_clear_thread.start()

# Main loop for the voice assistant
while True:
    user_input = listen()
    if not user_input:
        speak("Sorry, I didn't understand you. Could you repeat again?")
        continue

    # Check if navigation is running
    if navigation_running:
        if navigation_stop_phrase.lower() in user_input.lower():
            stop_navigation()
        else:
            speak("Navigation already running.")
        continue

    if re.search(command_pattern, user_input):
        user_tokens = word_tokenize(user_input.lower())
        for command, function in commands.items():
            if any(keyword in user_tokens for keyword in [command]):
                response = function()
                speak(response)

                # Check if the command started navigation
                if command == "navigation" or command == "start navigation":
                    start_navigation()

                break
        else:
            response = "Sorry, I couldn't understand your request."
            speak(response)

    # Check if the user said "Stop sensation"
    if "stop sensation" in user_input.lower():
        speak("Goodbye! See you again.")
        break
