import pyautogui
import os
import time

songname=input("Enter list of songs: \n")
print("Searching for " + songname)

os.system(r"C:\Users\inhor\AppData\Roaming\Spotify\Spotify.exe")
time.sleep(5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(songname, interval=0.1)

for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
    time.sleep(2)
    pyautogui.press(key)
