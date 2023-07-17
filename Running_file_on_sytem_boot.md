## Running_file_on_sytem_boot - README

### Introduction

This is the README file for the Sensation Voice Assistant, a Python script designed to provide various voice-assisted functionalities. The voice assistant utilizes the Vosk speech recognition model, various Python libraries, and external APIs to execute commands and respond to user requests.

### Functionality

The Sensation Voice Assistant can perform the following tasks:

- Retrieve the current time, date, and day of the week.
- Obtain the user's current location (city, region, country).
- Capture a picture from the connected camera and save it.
- Provide the option to shut down the system upon user confirmation.

### Requirements

Before running the Sensation Voice Assistant, ensure that the following dependencies are installed:

- Python 3.x
- The necessary Python packages specified in the code (cv2, datetime, requests, psutil, nltk, sounddevice, pyttsx3, geocoder, vosk, queue)
- A working internet connection to access external APIs

### Usage

To run the Sensation Voice Assistant:

1. Ensure that the required Python packages are installed in your environment.
2. If using a virtual environment, activate it before proceeding.
3. Run the `Sensation1.py` script using the Python interpreter:

```bash
python3 Sensation1.py
```

4. The voice assistant will welcome you with a greeting and begin listening for your commands.
5. You can interact with the voice assistant by speaking your commands.
6. To exit the voice assistant, say "Stop Sensation," and the assistant will gracefully terminate.

### Troubleshooting Method 1: Using `cron`

If Method 1: Using `cron` to run the script is not working, consider the following troubleshooting steps:

1. Check if the `cron` service is running on your Linux system.
2. Verify the correctness of the crontab entry, including the Python script path and any redirection of output.
3. Ensure that the Python script has execution permission (`chmod +x`).
4. Confirm that the correct Python interpreter path is used in the cron job.
5. Check for any external dependencies needed by the Python script when executed from `cron`.
6. Consider setting any required environment variables explicitly in the crontab file.

### Usage with Virtual Environment

If the Python script relies on a virtual environment, follow these steps to set up a `cron` job:

1. Activate the virtual environment containing the required Python packages.
2. Verify the correct Python interpreter path within the virtual environment.
3. Add the `cron` job specifying the virtual environment path and Python script path.
4. Reboot the system, and the `cron` job will execute the Python script within the virtual environment.

### Stopping the Voice Assistant

To stop the execution of the Python script and the Sensation Voice Assistant, you have several options:

1. Say "Stop Sensation," and the voice assistant will gracefully terminate.
2. Manually terminate the script by pressing `Ctrl + C` in the terminal or using the `kill` command with the process ID (PID).
3. Create a control script to send a specific signal to the running Python script, triggering its termination.

Remember to handle any necessary cleanup operations before stopping the script.

Enjoy using the Sensation Voice Assistant! Feel free to explore and modify the code to suit your preferences and needs. If you encounter any issues or have suggestions for improvement, please let us know. Happy voice-assisted interactions!
