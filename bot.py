import pyautogui
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
click(696,49)
time.sleep(2)
pyautogui.click(529, 294)
time.sleep(2)
pyautogui.click(532,343)
time.sleep(2)
pyautogui.click(254,191)
time.sleep(2)
pyautogui.click(537,825)
time.sleep(5)
# pyautogui.click(694,154)
# segunda tela:
pyautogui.click(466,877)
time.sleep(2)
pyautogui.click(542,776)
# controle segunda tela
time.sleep(2)
pyautogui.click(1417,50)
time.sleep(2)
pyautogui.click(1242,286)
time.sleep(2)
pyautogui.click(1248,341)
time.sleep(2)
pyautogui.click(929,213)
time.sleep(2)
pyautogui.click(1244,832)
time.sleep(5)
# pyautogui.click(1414,146)


# time.sleep(2)
# pyautogui.hotkey('alt', 'tab')
# time.sleep(5)
# pyautogui.click(686,50)
# while True: 
#     if pyautogui.locateOnScreen('youtube.png'):
#         print("esta na tela")
#     else:
#         print("Nao esta na tela") 
