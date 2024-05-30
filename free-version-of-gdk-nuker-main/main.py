import os
import sys
import pyfiglet
import subprocess

UTIL_FOLDER = "util"  # Define the name of the folder where the tools are located

# Define utility functions
def open_webhook_check():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "webhookcheck.py"))

def open_webhook_deleter_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "webhookdeleter.py"))

def open_nuker_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "nuker.py"))

# Main function
def main():
    ascii_banner = pyfiglet.figlet_format("GDK NUKER!")
    print(ascii_banner)
    print("\033[34mWelcome to GDK Nuker\033[0m")  # Blue color ANSI escape codes
    print("\033[34mPlease select an option:\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[1] account nuker\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[2] webhook checker\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[3] webhook deleter\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[4] cooming soon\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[5] cooming soon\033[0m")  # Blue color ANSI escape codes
    print("\033[34m[6] cooming soon \033[0m")  # Blue color ANSI escape codes
    choice = input("\033[34mEnter your choice: \033[0m")  # Blue color ANSI escape codes

    if choice == '1':
        open_nuker_py()
    elif choice == '2':
        open_webhook_check()
    elif choice == '3':
        open_webhook_deleter_py()
    elif choice == '4':
        ()
    elif choice == '5':
        ()
    elif choice == '6':
        ()
    else:
        print("\033[31mInvalid choice. Please select a valid option.\033[0m")  # Red color ANSI escape codes

if __name__ == "__main__":
    main()
