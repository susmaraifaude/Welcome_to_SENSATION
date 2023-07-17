import subprocess
import sys

# List all the required packages used in the code
required_packages = [
    "opencv-python",
    "requests",
    "psutil",
    "pyttsx3",
    "vosk",
    "sounddevice",
    "nltk",
    "geocoder",
]

# Check if pyinstaller is installed
try:
    import pyinstaller
except ImportError:
    print("PyInstaller is not installed. Please install it using 'pip install pyinstaller'")
    sys.exit(1)

# Check if the required packages are installed, and install them if missing
def check_and_install_packages():
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} has been installed successfully.")

def main():
    check_and_install_packages()

    # Replace 'your_script.py' with the name of your main Python script containing the code.
    script_file = "your_script.py"

    # Specify the name and options for the output executable
    options = [
        "--onefile",          # Create a single executable file
        "--windowed",         # Run the program without a console window (for GUI applications)
        "--name=Sensation",   # Name of the output executable file
        "--icon=icon.ico",    # Path to the icon file (if you want to use a custom icon)
    ]

    # Run PyInstaller to create the executable
    subprocess.check_call(["pyinstaller"] + options + [script_file])

if __name__ == "__main__":
    main()
