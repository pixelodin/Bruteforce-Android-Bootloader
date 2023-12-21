import subprocess
import itertools
import time

def progress_bar(device, key, progress, length):
    print(f"\rKey: {key} [{'#' * progress}{' ' * (length - progress)}] {device}", end='', flush=True)

def save_progress(device, value):
    print("\nSaving progress...")
    with open(f"./{device}.dat", "w") as f:
        f.write(value)

def is_unlock_allowed(device):
    try:
        output = subprocess.check_output(["fastboot", "getvar", "unlock-allowed"], text=True)
        return "True" in output
    except subprocess.CalledProcessError:
        return False

def main():
    devices_raw = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
    devices = devices_raw.stdout.strip().split('\n')
    if not devices:
        print("No device found")
        exit()

    device = devices[0]
    print(f"Current device: {device}")

    devfile = f"./{device}.dat"
    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    min_length = 1
    max_length = 8
    value = ""

    tried_combinations = set()

    if not is_unlock_allowed(device):
        for length in range(min_length, max_length + 1):
            combinations = itertools.product(charset, repeat=length)
            for combination in combinations:
                value = ''.join(combination)
                progress_bar(device, "Searching for unlock code", 0, 100)

                if value not in tried_combinations and is_unlock_allowed(device):
                    output = subprocess.run(["fastboot", "oem", "unlock", value], capture_output=True, text=True)

                    if "FAILED" not in output.stdout:
                        print(f"\nYour unlock code is: {value}")
                        print(f"Saving unlock code to {devfile}...")
                        save_progress(device, value)
                        return  # Exit if unlock code is found

                    tried_combinations.add(value)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"\nExecution time: {time.time() - start_time} seconds")
