import pyautogui
import pyperclip
import os
import time
import sys

inputs = [] 
input1 = input("Enter song: ") 
while input1 != "": 
	inputs.append(input1) 
	input1 = input("Enter song: ")


for i in inputs:
    print("Searching for " + i)

    os.system(r"C:\Users\inhor\AppData\Roaming\Spotify\Spotify.exe")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    pyperclip.copy(i)
    pyautogui.hotkey("ctrl", "v")
    #pyautogui.write(i, interval=0.1)

    for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
        time.sleep(2)
        pyautogui.press(key)
    time.sleep(10)
    pyautogui.press('space')
