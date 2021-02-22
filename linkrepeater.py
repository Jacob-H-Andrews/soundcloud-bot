import webbrowser
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()

for i in range(40):
    webbrowser.open('https://soundcloud.com/jhakeuk/intentionsdnb')
    time.sleep(3)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
