#code
import pyautogui 
from PIL import Image, ImageGrab 
import time

def click(key):
    pyautogui.keyDown(key)
    return

def Collision(data):
#Crouch for birds
    for i in range(530,560):
        for j in range(80, 127):
            if data[i, j] < 171:
                click("down")
                return
 #Jump for cactus
    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] < 100:
                click("up")
                return
    return
if __name__ == "__main__":
    time.sleep(5)
    click('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        Collision(data)
