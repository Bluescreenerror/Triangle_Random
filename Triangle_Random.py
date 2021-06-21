import pyautogui  
import time 
import math
import random
list1 = [1137, 70, 1131, 98, 1106, 73, 1104, 100, 1079, 70, 1045, 98, 997, 78]
l = 200
hypotenuse = l
l1 = []
pyautogui.press("Win")
pyautogui.typewrite("Paint")
pyautogui.press("Enter")
time.sleep(0.5)
pyautogui.moveTo(730, 80, 0.2)
pyautogui.click()
time.sleep(0.2)
pyautogui.move(0, 250, 0.2)
pyautogui.click()
time.sleep(1)

while True:
    triangle_type = random.randint(0,1)
    a = random.randrange(230, 1820)
    b = random.randrange(346, 1030)
    if triangle_type == 1:
        if a and b in l1:
            continue
        else:
            j = random.randint(0,13)
            if j % 2 == 0: 
                x_c = list1[j]
                y_c = list1[j + 1]
            else:
                x_c = list1[j - 1]
                y_c = list1[j]
                pyautogui.moveTo(x_c, y_c)
                pyautogui.click()
                time.sleep(0.2)
                pyautogui.moveTo(a-l, b)
                pyautogui.drag(l,0)
                p = hypotenuse * math.sin(math.pi/3)
                q = hypotenuse * math.cos(math.pi/3)
                pyautogui.drag(-q,-p)
                pyautogui.drag(-q, p)
                l1.append(a)
                l1.append(b)
                triangle_type = random.randint(0,1)
    
    else:
        a = random.randint(230, 1820)
        b = random.randint(280, 700)
        if a and b in l1:
            continue
        else:
            j = random.randint(0,13)
            if j % 2 == 0: 
                x_c = list1[j]
                y_c = list1[j + 1]
            else:
                x_c = list1[j - 1]
                y_c = list1[j]
                pyautogui.moveTo(x_c, y_c)
                pyautogui.click()
                time.sleep(0.2)
                pyautogui.moveTo(a-l, b)
                pyautogui.drag(l,0)
                p = hypotenuse * math.sin(math.pi/3)
                q = hypotenuse * math.cos(math.pi/3)
                pyautogui.drag(-q,p)
                pyautogui.drag(-q,-p)
                l1.append(a)
                l1.append(b)
