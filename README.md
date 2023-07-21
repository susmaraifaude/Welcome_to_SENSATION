# Sensation Voice Assistant - README

## Description

Sensation is a voice-controlled assistant built in Python. It can perform various tasks such as providing the current time and date, fetching your location, taking pictures, and shutting down your system, among others. The assistant uses the Vosk speech recognition model for voice input and the pyttsx3 library for text-to-speech output.

## Dependencies

The following python libraries are required for the implementation:

- os
- cv2 (OpenCV)
- datetime
- requests
- psutil
- re
- json
- time
- threading
- nltk
- sounddevice
- pyttsx3
- geocoder
- vosk
- queue

We have provided a build file that installs all the above required dependencies and runs the python program Sensation1.py automatically:
```
python build.py
```

Alternatively, You can install the required dependencies using pip:

```
pip install opencv-python datetime requests psutil nltk sounddevice pyttsx3 geocoder vosk
```

Also, make sure to download the NLTK tokenizer data by running the following in your Python environment:

```python
import nltk
nltk.download('punkt')
```

## Setup

1. **Vosk Language Model**: To use the Vosk speech recognition model, you need to download the appropriate model for your language. Replace `"path/vosk-model-small-en-in-0.4"` in the code with the actual path to your Vosk language model. You can download the model for your language from the Vosk GitHub repository: https://github.com/alphacep/vosk-api/tree/master/model

- Make sure you have up-to-date pip and python3 versions:
  **Python version**: 3.5-3.9
  **pip version**: 20.3 and newer.

2. **Camera Access**: For taking pictures, the code uses OpenCV (`cv2`) to access the camera. Make sure you have a camera connected to your computer, and the OpenCV library is properly installed.

3. **User Picture Folder**: In the `take_picture()` function, replace `"C:/Users/Pictures/Clicked pictures"` with the path where you want to save the captured pictures.

## How to Use

1. Run the script in your Python environment, and the Sensation assistant will welcome you.

2. The assistant listens to your voice input. Just say the trigger word "Sensation" followed by a specific command (e.g., "Sensation, what's the time?").

3. The assistant will recognize your command and perform the corresponding task.

4. For the "shutdown_system" command, the assistant will ask for your confirmation before shutting down the system.

5. To exit the assistant, simply say "Stop Sensation," and it will bid you goodbye.

## Supported Commands

- `time`: Get the current time.
- `date`: Get today's date.
- `day`: Get the current day.
- `position`, `address`, `location`, `where am i now`: Get your current location.
- `picture`, `photo`, `selfie`, `shot`: Take a picture using the connected camera and save it.
- `shut`, `down`, `turn`, `off`: Shut down the system. The assistant will ask for confirmation before proceeding.
- `stop`: Stop the voice assistant and exit.

**Note**: The assistant is designed to recognize the specific trigger word "Sensation" followed by a valid command from the list above. If you encounter issues with command recognition, try speaking clearly and ensure that the command you want to execute is included in the list of supported commands.

## Important Considerations

- The Vosk language model is responsible for recognizing your voice commands. Please ensure you have the correct model loaded and it supports your language.
- The camera access is necessary for the `take_picture()` function to work correctly.
- Be cautious when using the "shut down" command, as it will immediately shut down your system without further confirmation.
- This code is designed for educational purposes and may require additional error handling and improvements for production use.
