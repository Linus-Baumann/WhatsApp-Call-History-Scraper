import cv2
import os
from skimage.metrics import structural_similarity as compare_ssim

def top_of_chat_reached(screenshot_directory, iteration):
    print("Comparing screenshots...")
    current_image = cv2.imread(os.path.join(screenshot_directory, f"chat_{iteration}.png"), cv2.IMREAD_GRAYSCALE)
    last_image = cv2.imread(os.path.join(screenshot_directory, f"chat_{iteration - 1}.png"), cv2.IMREAD_GRAYSCALE)
    score, _ = compare_ssim(current_image, last_image, full=True)
    return score >= 0.99