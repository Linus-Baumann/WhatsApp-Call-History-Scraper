import cv2

def mark_regions(image, regions, show=False,output_path=None, color=(0, 255, 0), thickness=2):
    """
    Marks multiple regions in the image with numbered rectangles, and optionally saves or displays the output.

    Args:
        image (str or numpy.ndarray): The path to the image file or a loaded image as a NumPy array.
        regions (list of tuples): A list of regions, where each region is a tuple (x, y, width, height).
        output_path (str, optional): The file path where the output image will be saved. Required if `save=True`.
        color (tuple): The color of the rectangle and text in BGR format. Default is green (0, 255, 0).
        thickness (int): The thickness of the rectangle borders. Default is 2.
        show (bool): Whether to display the image with the marked regions. Default is False.
        save (bool): Whether to save the image with the marked regions. Default is False.
    
    Returns:
        None
    """
    # Load the image if a path is provided
    if isinstance(image, str):
        img = cv2.imread(image)
        if img is None:
            raise FileNotFoundError(f"Image not found at {image}")
    else:
        img = image.copy()
    
    # Font settings for numbering
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 1
    
    # Loop through the regions and mark each one
    for i, region in enumerate(regions, start=1):
        (x, y, w, h) = region['region']
        
        # Draw the rectangle around the region
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        
        # Add the region number near the top-left corner of the rectangle
        text = str(i)
        text_position = (x, y - 5)  # Slightly above the rectangle
        cv2.putText(img, text, text_position, font, font_scale, color, font_thickness)
    
    # Show the image if requested
    if show:
        cv2.imshow("Highlighted Regions", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # Save the image if requested
    if not show:
        if output_path is None:
            raise ValueError("You must provide an output_path if save=True")
        cv2.imwrite(output_path, img)
        print(f"Output image with marked regions saved at {output_path}")

