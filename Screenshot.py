import pyautogui

def takeScreenshot():
    image = pyautogui.screenshot()
    image.save('./ss.png')