# importing modules
import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw The Rectangle for birds
    for i in range(323, 373):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit('down')
                return

    # Draw Rectangle for cactus
    for i in range(323, 373):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit('up')
                return
    return

if __name__ == '__main__':
    print('Hey!! Dino Game is about to start in 3 seconds')
    time.sleep(3)
    # hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')
        '''
        # Draw The Rectangle for cactus
        for i in range(320, 370):
            for j in range(563, 650):
                data[i, j] = 0
        
        # Draw The Rectangle for birds
        for i in range(320, 370):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
'''