import pyautogui
pyautogui.sleep(2)

spam = open('spam', 'r')

for words in spam:
    pyautogui.typewrite(words)
    pyautogui.press('enter')
