import subprocess
import ctypes
import threading
from time import sleep
from datetime import datetime as dt


def kill_app(name, start, end):
    while True:
        if (
            start
            < dt.now()
            < end
        ):
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            while True:
                subprocess.call(f'taskkill /F /IM {name}', startupinfo=si)
                # ctypes.windll.user32.MessageBoxW(0, 'Get back to work!', 'Alert!', 0)
                sleep(1)  # delay 1 seconds
                if dt.now() > end:
                    print("Bye , END")
                    break
        else:
            print("Fin Big While")
            ctypes.windll.user32.LockWorkStation()
            break

if __name__ == "__main__":
    names = open('blocked_apps.txt', 'r').read().split('\n')
    s = e = 0
    try:
        s = int(input("Enter Starting Hour: "))
        e = int(input("Enter Ending Hour: "))

    except:
        ctypes.windll.user32.MessageBoxW(
            0, 'Enter Valid Number!', 'Alert!', 0)

    if s and e:
        for i in names:
            if i:
                iThread = threading.Thread(target=kill_app, args=(i, s, e))
                iThread.start()
