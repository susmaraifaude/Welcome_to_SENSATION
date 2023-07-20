## Running_file_on_sytem_boot - README




## Start on Boot : Using `cron`

Using `cron` to run the script is not working, consider the following troubleshooting steps:

## Usage with Virtual Environment

If the Python script relies on a virtual environment, follow these steps to set up a `cron` job:

1. Activate the virtual environment containing the required Python packages:

   ```bash
   source /path/to/your/virtualenv/bin/activate
   ```

2. **Check if Cron is Running**: First, ensure that the `cron` service is running on your Linux system. Open a terminal and check the status of the `cron` service:

   ```bash
   sudo systemctl status cron
   ```

   If the service is not active, start it with:

   ```bash
   sudo systemctl start cron
   ```

   Additionally, enable the service to start automatically on boot:

   ```bash
   sudo systemctl enable cron
   ```

3. Verify the correct Python interpreter path within the virtual environment:

   ```bash
   which python
   ```

4. Open a terminal and enter the crontab -e command to open the crontab editor and Add the `cron` job specifying the virtual environment path and Python script path:

   ```bash
   @reboot /path/to/your/virtualenv/bin/python /path/to/Sensation1.py >> /path/to/logfile.log 2>&1
   ```

5. Save the crontab by pressing Ctrl+X and then Y and exit the editor.

6. Reboot the system, and the `cron` job will execute the Python script within the virtual environment.

## Stopping the Voice Assistant

To stop the execution of the Python script and the Sensation Voice Assistant, you have several options:

1. Say "Stop Sensation," and the voice assistant will gracefully terminate.
2. Manually terminate the script by pressing `Ctrl + C` in the terminal or using the `kill` command with the process ID (PID).
3. Create a control script to send a specific signal to the running Python script, triggering its termination.
