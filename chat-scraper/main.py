from src.automation import locate_whatsapp_window, scroll_chat
from src.screen_capture import capture_chat_region, save_screenshot
from src.screen_analysis import top_of_chat_reached
import os
import time

def main():
    # Configuration
    output_dir = f"data/screenshots/{time.strftime('%Y-%m-%d')}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Locate WhatsApp window
    whatsapp_window = locate_whatsapp_window()
    region = (whatsapp_window.left, whatsapp_window.top, whatsapp_window.width, whatsapp_window.height)
    print(f"Located WhatsApp window at {region}.")

    iteration = 0

    # Capture and scroll
    while True:
        print("==================\nIteration: ", iteration)
        screenshot = capture_chat_region(region)
        screenshot_path = os.path.join(output_dir, f"chat_{iteration}.png")
        save_screenshot(screenshot, screenshot_path)

        if iteration!=0 and top_of_chat_reached(output_dir, iteration):
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)
            break
        scroll_chat()
        print("==================\n")
        iteration += 1
        time.sleep(1)

if __name__ == "__main__":
    main()