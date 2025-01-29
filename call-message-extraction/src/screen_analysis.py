import cv2
import os
import numpy as np
from src.debug_helper import mark_regions


def extract_call_message_regions_from_image(image, template_path='./data/templates/', threshold=0.8):
    """
    Detect regions in the chat screenshot where the call messages are located.
    :param image_path: Path to the full chat screenshot.
    :param template_path: Path to the template of the call message.
    :param threshold: Similarity threshold for template matching (default: 0.8).
    :return: List of bounding boxes for detected call messages.
    """
    # Load the full screenshot and template
    voice_call_template = cv2.imread(os.path.join(template_path, 'voice-call_template.png'), cv2.IMREAD_GRAYSCALE)
    video_call_template = cv2.imread(os.path.join(template_path, 'video-call_template.png'), cv2.IMREAD_GRAYSCALE)

    # Convert the full screenshot to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    call_message_regions = []
    call_message_regions.extend(extract_voice_call_messages(gray_image, voice_call_template, threshold))
    call_message_regions.extend(extract_video_call_messages(gray_image, video_call_template, threshold))

    return call_message_regions

def extract_voice_call_messages(image, video_call_template, threshold):
    messages = extract_voice_call_locations(image, video_call_template, threshold)
    call_message_regions = []
    for message in messages:
        message['region'] = (int(message['region'][0] + message['region'][2]), int(message['region'][1] + 0.5 * message['region'][3]), message['region'][2] * 4, int(message['region'][3] * 0.5))
        call_message_regions.append(message)
    return call_message_regions

def extract_voice_call_locations(image, voice_call_template, threshold, nms_threshold=0.3):
    """
    Extract video call message regions using template matching and apply non-maximum suppression (NMS)
    to ensure each message is only recognized once.

    Args:
        image (numpy.ndarray): The input image.
        voice_call_template (numpy.ndarray): The template image for a video call message.
        threshold (float): The similarity threshold for template matching (0.0 to 1.0).
        nms_threshold (float): The threshold for non-maximum suppression. Lower values = stricter suppression.
        show (bool): If True, shows the regions on the image.

    Returns:
        List[Tuple[int, int, int, int]]: A list of unique regions (x, y, width, height) for video call messages.
    """
    # Perform template matching
    result = cv2.matchTemplate(image, voice_call_template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)  # Get all matching locations

    # Define bounding boxes for matches
    h, w = voice_call_template.shape[:2]
    boxes = []
    for pt in zip(*locations[::-1]):  # Switch x and y axes
        x, y = pt
        boxes.append([x, y, x + w, y + h])  # Convert to (x1, y1, x2, y2) format

    # Apply non-maximum suppression (NMS)
    boxes = np.array(boxes)
    if len(boxes) > 0:
        indices = cv2.dnn.NMSBoxes(boxes.tolist(), [1.0] * len(boxes), score_threshold=0.0, nms_threshold=nms_threshold)
        if len(indices) > 0:
            indices = indices.flatten()  # Extract valid box indices
            unique_regions = [boxes[i] for i in indices]
        else:
            unique_regions = []
    else:
        unique_regions = []

    # Convert back to (x, y, width, height) format
    voice_call_message_regions = []
    for x1, y1, x2, y2 in unique_regions:
        region = (x1, y1, x2 - x1, y2 - y1)
        voice_call_message_regions.append({
            'region': region,
            'type': 'Voice'
        })

    return voice_call_message_regions

def extract_video_call_messages(image, video_call_template, threshold):
    messages = extract_video_call_message_locations(image, video_call_template, threshold)
    call_message_regions = []
    for message in messages:
        message['region'] = (int(message['region'][0] + message['region'][2]), int(message['region'][1] + 0.5 * message['region'][3]), message['region'][2] * 4, int(message['region'][3] * 0.5))
        call_message_regions.append(message)
    return call_message_regions

def extract_video_call_message_locations(image, video_call_template, threshold, nms_threshold=0.3):
    """
    Extract video call message regions using template matching and apply non-maximum suppression (NMS)
    to ensure each message is only recognized once.

    Args:
        image (numpy.ndarray): The input image.
        video_call_template (numpy.ndarray): The template image for a video call message.
        threshold (float): The similarity threshold for template matching (0.0 to 1.0).
        nms_threshold (float): The threshold for non-maximum suppression. Lower values = stricter suppression.
        show (bool): If True, shows the regions on the image.

    Returns:
        List[Tuple[int, int, int, int]]: A list of unique regions (x, y, width, height) for video call messages.
    """
    # Perform template matching
    result = cv2.matchTemplate(image, video_call_template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)  # Get all matching locations

    # Define bounding boxes for matches
    h, w = video_call_template.shape[:2]
    boxes = []
    for pt in zip(*locations[::-1]):  # Switch x and y axes
        x, y = pt
        boxes.append([x, y, x + w, y + h])  # Convert to (x1, y1, x2, y2) format

    # Apply non-maximum suppression (NMS)
    boxes = np.array(boxes)
    if len(boxes) > 0:
        indices = cv2.dnn.NMSBoxes(boxes.tolist(), [1.0] * len(boxes), score_threshold=0.0, nms_threshold=nms_threshold)
        if len(indices) > 0:
            indices = indices.flatten()  # Extract valid box indices
            unique_regions = [boxes[i] for i in indices]
        else:
            unique_regions = []
    else:
        unique_regions = []

    # Convert back to (x, y, width, height) format
    video_call_message_regions = []
    for x1, y1, x2, y2 in unique_regions:
        region = (x1, y1, x2 - x1, y2 - y1)
        video_call_message_regions.append({
            'region': region,
            'type': 'Video'
        })

    return video_call_message_regions