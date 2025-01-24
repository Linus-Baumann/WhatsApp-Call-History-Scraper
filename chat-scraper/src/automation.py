import pyautogui
import pygetwindow as gw
import time

def locate_whatsapp_window():
    print("Please open the WhatsApp window and switch to the chat you want to scrape.")
    print("Waiting for 5 seconds...")
    time.sleep(5)
    return gw.getActiveWindow()

def scroll_chat(delay=1):
    pyautogui.press("pageup", presses=1)
    time.sleep(0.5)
    pyautogui.press("down", presses=3, interval=0.1)
    print("Scrolled chat.")
