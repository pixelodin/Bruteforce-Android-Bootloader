# Bruteforce-Android-Bootloader
Bruteforce Bootloader Unlocker for android smartphones with fastboot support. 

This is a bash script that tries to unlock the bootloader of Android devices using fastboot.

## Requirements

- Linux or windows operating system
- Fastboot and adb installed
- USB debugging enabled on your device

## Usage

1. Connect your device to your computer via USB cable
2. Run `chmod +x Bruteforce` to make the script executable
3. Run `./Bruteforce` to start the bruteforce process
4. The script uses a combination of numbers (0-9) and lowercase letters (a-f) in the unlock code, with a range of 0-255. You can further customize the alphabet array and the min_code, max_code, and step variables to suit your needs.
5. The script will save the current value in a persistent file every time it exits, so you can resume from where you left off
6. If the script finds your unlock code, it will display it on the screen and exit

## Instructions for using the Python version of the script:

    Connect your device to your computer using a USB cable.
    Enable USB debugging on your device by going to Settings > Developer options > USB debugging.
    Open a terminal or command prompt and navigate to the directory where the script is saved.
    Run the script by executing the command python3 script_name.py.
    When prompted, select your device from the list of connected devices.
    Wait for the script to finish.
    Once the script finishes, check the .dat file associated with your device for the unlock code.

## Note that the script assumes that you have the fastboot tool installed on your system. If you don't have it installed, you can install it using the following command:

    For Ubuntu: sudo apt-get install android-tools-adb
    For macOS: brew install android-platform-tools
    For Windows: Download and install the Android SDK Platform Tools package from the official Android developer website.

## Also, note that the script has not been extensively tested and may require additional modifications depending on your specific device and environment. Use at your own risk and make sure to backup any important data before running the script.



## The modifications I made include:

    Adding uppercase letters and numbers to the alphabet array
    Updating the range of the min_code, max_code, and index variables to include the entire alphabet array
    Updating the value of value to include the next character in the alphabet array instead of incrementing the ASCII value of the current character.



# Keep in mind that the length of the alphabet array and the max_code value should be adjusted if you want to use more characters or a longer unlock code.

# Please note that this example is specific to numbers and lowercase letters. You can modify the alphabet array to include uppercase letters, symbols, or other characters

## Disclaimer

This script is for educational purposes only. Use it at your own risk. I am not responsible for any damage or data loss that may occur as a result of using this script.
