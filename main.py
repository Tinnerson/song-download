import pyautogui
import os
import time
import sys

inputs = [] 
input1 = input("What is the input? ") 
while input1 != "": 
	inputs.append(input1) 
	input1 = input("What is the input? ")


for i in inputs:
    print("Searching for " + i)

    os.system(r"C:\Users\inhor\AppData\Roaming\Spotify\Spotify.exe")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(i, interval=0.1)

    for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
        time.sleep(2)
        pyautogui.press(key)
    time.sleep(10)
    pyautogui.press('space')
