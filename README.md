Alarm Clock

A simple, user-friendly **alarm clock desktop application** built with Python and **Tkinter**.

Set a time → the app waits → plays a sound and shows a醒醒 message when it's time!  
Perfect mini-project to learn GUI programming, time handling, threading, and sound playback in Python.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-included-success?logo=python&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/github/license/shahinabbasidev/Alarm_Clock?color=green" alt="License: MIT">
</p>

✨ Features

- Clean graphical interface using **Tkinter**
- Set alarm hour, minute, and optional AM/PM
- Real-time clock display
- Plays sound when alarm triggers (using `winsound` on Windows or `pygame` / system sound elsewhere)
- Thread-safe alarm checking (doesn't freeze the GUI)
- Simple "Alarm Ringing!" popup + sound alert

📸 Screenshot

(Add your own screenshot here later!)

<!-- Placeholder – replace with real image -->
<!-- ![Alarm Clock GUI](docs/screenshot.png) -->

Example look: time picker + current time label + "Set Alarm" button.

🚀 Quick Start

Prerequisites

- Python 3.8 or higher
- Tkinter (usually comes pre-installed with Python)

Installation & Run

```bash
git clone https://github.com/shahinabbasidev/Alarm_Clock.git
cd Alarm_Clock

# Just run it — no extra dependencies needed if using winsound (Windows)
python alarm.py    

🛠️ Tech Stack

Language: Python 3
GUI: Tkinter (standard library)
Sound (optional): winsound (Windows built-in) or pygame
Concurrency: threading (to check time without blocking GUI)

