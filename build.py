import subprocess
import importlib
import os

def install_dependencies(packages):
    for package in packages:
        try:
            importlib.import_module(package)
        except ImportError:
            subprocess.run(["pip", "install", package])  

def run_sensation1():
    subprocess.run(["python", "Sensation1.py"])

if __name__ == "__main__":
    dependencies = ["nltk", "opencv-python", "requests", "psutil", "sounddevice", "pyttsx3", "geocoder", "vosk"]
    install_dependencies(dependencies)
    # Download the NLTK data
    import nltk
    nltk.download("punkt")
    run_sensation1()
