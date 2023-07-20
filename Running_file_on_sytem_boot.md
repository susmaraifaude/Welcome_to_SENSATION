## Running_file_on_sytem_boot - README




## Start on Boot : Using `cron`

Using `cron` to run the script is not working, consider the following troubleshooting steps:

1. Check if the `cron` service is running on your Linux system:

   ```bash
   sudo systemctl status cron
   ```

2. Verify the correctness of the crontab entry, including the Python script path and any redirection of output.
3. Ensure that the Python script has execution permission (`chmod +x`).
4. Confirm that the correct Python interpreter path is used in the cron job.
5. Check for any external dependencies needed by the Python script when executed from `cron`.
6. Consider setting any required environment variables explicitly in the crontab file.

## Usage with Virtual Environment

If the Python script relies on a virtual environment, follow these steps to set up a `cron` job:

1. Activate the virtual environment containing the required Python packages:

   ```bash
   source /path/to/your/virtualenv/bin/activate
   ```

2. Verify the correct Python interpreter path within the virtual environment:

   ```bash
   which python
   ```

3. Open a terminal and enter the crontab -e command to open the crontab editor and Add the `cron` job specifying the virtual environment path and Python script path:

   ```bash
   @reboot /path/to/your/virtualenv/bin/python /path/to/Sensation1.py >> /path/to/logfile.log 2>&1
   ```

4. Save the crontab by pressing Ctrl+X and then Y and exit the editor.

5. Reboot the system, and the `cron` job will execute the Python script within the virtual environment.

## Stopping the Voice Assistant

To stop the execution of the Python script and the Sensation Voice Assistant, you have several options:

1. Say "Stop Sensation," and the voice assistant will gracefully terminate.
2. Manually terminate the script by pressing `Ctrl + C` in the terminal or using the `kill` command with the process ID (PID).
3. Create a control script to send a specific signal to the running Python script, triggering its termination.
