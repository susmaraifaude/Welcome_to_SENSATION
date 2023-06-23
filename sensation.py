#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pyttsx3
import speech_recognition as sr
import subprocess
import time
import os
import time
import sys
import geocoder

# In[35]:


def play_audio_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

def stop_sensation():
    # Stop the running loop and output "Bye"
    play_audio_text("Bye see you next time")
    sys.exit()

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g
    else:
        return None

def say_position():
    # Say the user's position
    location = get_current_location()
    if location:
        play_audio_text("You are at "+location.city)
    else:
        play_audio_text("Sorry! Can't determine current location.")

def get_current_time():
    # Get the current time
    current_time = time.strftime("%H:%M")
    output_text = f"It is {current_time}"
    play_audio_text(output_text)

def get_speech_input():
    # Get speech input from the user    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
    return ""


# In[33]:


def main():
    # Welcome message
    play_audio_text("Welcome to SENSATION")

    while True:
        command = get_speech_input()
        if command.lower() == "start sensation":
            play_audio_text("SENSATION started")
        elif command.lower() == "stop sensation":
            stop_sensation()
            break  # Exit the while loop after stopping sensation
        elif command.lower() == "location":
            say_position()
        elif command.lower() == "time" or command.lower() == "what is the time":
            get_current_time()
        elif command.lower() == "shutdown sensation":
            play_audio_text("Should the system really shutdown? Please say yes or no.")
            response = get_speech_input()
            if response.lower() == "yes":
                play_audio_text("Shutting down the system")
                # Uncomment the following line to actually perform system shutdown
                # subprocess.call(["shutdown", "/s", "/t", "0"])
            else:
                play_audio_text("System will not shutdown.")
        else:
            play_audio_text("Invalid command")

if __name__ == "__main__":
    main()







