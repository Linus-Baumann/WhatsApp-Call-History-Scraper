import pyautogui

def capture_chat_region(region):
    screenshot = pyautogui.screenshot(region=region)
    print("Captured screenshot.")
    return screenshot

def save_screenshot(image, path):
    image.save(path)
    print(f"Saved screenshot to {path}.")