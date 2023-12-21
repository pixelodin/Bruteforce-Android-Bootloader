#!/usr/bin/env python3

import subprocess
import time

# Function to display progress bar
def progress_bar(device, key, progress, length):
    print(f"\rKey: {key} [{key[:length]}]{'#' * progress}", end='')
    time.sleep(0.01)

# Function to save progress
def save_progress(device, value):
    with open(f"./{device}.dat", "w") as f:
        f.write(value)

# Function to load progress
def load_progress(device):
    try:
        with open(f"./{device}.dat", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

# Get device name from fastboot
devices = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
device = devices.strip()
if not device:
    print("No device found")
    exit()

# Create file name based on device name
devfile = f"./{device}.dat"

# Define the alphabet for the unlock code
alphabet = (
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
)

# Define the range and pattern of unlock codes
min_code = 0
max_code = len(alphabet) - 1
step = 1

# Initialize the value string
value = ""

# Check if device is in bootloader mode
if not is_bootloader(device):
    print(f"Device {device} is not in bootloader mode. Exiting...")
    exit()

# Load progress if file exists
value = load_progress(device)
if value:
    # Get the index of the current value in the alphabet array
    index = alphabet.index(value)
else:
    # Initialize the index to the minimum value
    index = min_code

# Check if device is in "UNLOCK THE BOOTLOADER" screen
while True:
    # Display progress bar
    progress_bar(device, value, index, len(alphabet))

    # Check if device is in "UNLOCK THE BOOTLOADER" screen
    if is_unlock_screen(device):
        # Try to unlock device with fastboot
        output = subprocess.run(["fastboot", "oem", "unlock", value], capture_output=True, text=True)

        # Check if unlock code was found
        if "FAILED" not in output:
            print(f"\nYour unlock code is: {value}")
            print(f"Saving unlock code to {devfile}...")
            save_progress(device, value)
            break

    # Increment value for next try
    index += step

    # Set the value to the next character in the alphabet array
    if index < 0:
        index = max_code
    elif index > max_code:
        index = min_code
    value = alphabet[index]
