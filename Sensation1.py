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

nltk.download('punkt')

# Loading the vosk model
model = Model("path/vosk-model-small-en-in-0.4")  # Replace "path/to/your/vosk/model" with the actual path to your Vosk language model or keep it in the same python file 


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


# Function to get the current location
def get_location():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        city = data['city']
        region = data['region']
        country = data['country_name']

        if 'location' in data and 'street' in data['location']:
            street = data['location']['street']
            return f"You are currently in {street}, {city}, {region}, {country}"
        else:
            return f"You are currently in {city}, {region}, {country}"
    except requests.exceptions.RequestException:
        return "Sorry, I couldn't retrieve the location."

# Function to take a picture and save it
def take_picture():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    camera.release()

    if return_value:
        folder_path = "C:/Users/Srinjoy Ghosh/Pictures/Clicked pictures"  # Replace <your_username> with your Windows username
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

# Welcome message
speak("Welcome to Sensation! How can I assist you?")

# A dictionary to map commands to functions
commands = {
    "time": get_time,
    "date": get_date,
    "day": get_day,
    "position": get_location,
    "location": get_location,
    "address": get_location,
    "where am i now": get_location,
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
command_pattern = re.compile(rf"(?i)\b{trigger_word}\b.*\b(?:time|date|day|position|address|location|picture|photo|selfie|shot|shut|down|turn|off|stop|city|state|country|street)\b")


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

    if re.search(command_pattern, user_input):
        user_tokens = word_tokenize(user_input.lower())
        for command, function in commands.items():
            if any(keyword in user_tokens for keyword in [command]):
                response = function()
                speak(response)
                break
        else:
            response = "Sorry, I couldn't understand your request."
            speak(response)

    # Check if the user said "Stop sensation"
    if "stop sensation" in user_input.lower():
        speak("Goodbye! See you again.")
        break
