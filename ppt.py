import keyboard
import subprocess
import os
import time
import random

while True:
    # Running the aforementioned command and saving its output
    output = os.popen('wmic process get description, processid').read()
    if (output.find("POWERPNT") > 0 ):
        print('Powerpoint open!')
        break
while True:
    if (keyboard.is_pressed('f5')):
        print('start!')
        break


detect_cmd = 'darknet.exe detector demo yolo.data cfg/yolov4-custom.cfg backup/yolov4-custom_final.weights -c 0'
detect = subprocess.Popen(detect_cmd, shell=True)
flag = 1
time.sleep(2)
while True:
    for i in range(50000):
        if (keyboard.is_pressed('esc')):
            flag = 0
            break
    if (flag == 0):
         break
    f = open("result.txt","r")
    result = f.readlines()
    if result:
        result_list = []
        for line in result:
            a = line.strip()
            result_tuple = (int(a[a.find(':')+2:a.find('%')]),a[0:a.find(':')])
            result_list.append(result_tuple)
        result_list.sort(reverse = True)
        result = result_list[0][1]
        print('keyboard',result)
        keyboard.press(result)
detect.terminate()




