# Lock:
import ctypes
import os
import datetime


def Lock_Pc():
    ctypes.windll.user32.LockWorkStation()

# Change Dns:
import subprocess
def dns_change():
    si = subprocess.STARTUPINFO()
    subprocess.run(f'ipconfig /flushdns')
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.run(
        f'netsh interface ip set dns name = "Wi-Fi" static 208.67.222.123')
    subprocess.call(
        f'netsh interface ip add dns name = "Wi-Fi" 208.67.220.123 index = 2', startupinfo=si)

dns_change()


# Get Domain Ip For WhiteList:
import socket


def Get_ip(host):
    socket.gethostbyname(host)  # => 'ip'
# we will use this List : https://pastebin.com/63hfPx8M



# Get Last X items from All History : we should kill browser process for update
import browser_history
from datetime import datetime

def get_history():
    date_time_str = input("Enter Date Like 'yyyy-mm-dd hh:mm:ss' : ")
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    outputs = browser_history.get_history()
    H = outputs.to_csv().replace('\r', '').split('\n')[::-1][1:]
    # print(H)
    for i in H:
        h = i.split(',')
        date = h[0][:-6]
        url = h[1]
        date_dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if date_dt > date_time_obj:
            print(f"{date} : {url}")


# Block App from Running:
import subprocess
from time import sleep

# bloqui les app
def kill_app1(x):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    while True:
        subprocess.call(f'taskkill /F /IM {x}', startupinfo=si)
        sleep(1)  # delay 1 seconds



import subprocess
from time import sleep
import ctypes
import threading


# def kill_app(name):
#     si = subprocess.STARTUPINFO()
#     si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#     while True:
#         subprocess.call(f'taskkill /F /IM {name}', startupinfo=si)
#         # ctypes.windll.user32.MessageBoxW(
#         #     0, 'Get back to work!', 'Alert!', 0)
#         sleep(1)  # delay 1 seconds
#
# names = open('blocked_apps.txt', 'r').read().split('\n')
# print(names)
# # print(name)
#
# for i in names:
#     if i:
#         iThread = threading.Thread(target=kill_app, args=(i,))
#         iThread.start()


get_history()