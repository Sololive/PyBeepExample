import ctypes
from time import sleep
import os
def Main():
    kernel32 = ctypes.WinDLL("Kernel32")
    kernel32.Beep(500, 500)
    print("This Python Script is Beeped Successfully!!!")
    sleep(7)
    os._exit(554)

if __name__ == "__main__":
    Main()