from PIL import Image
import numpy as np
from scipy.ndimage import label

def select_largest_subject(image: Image.Image) -> Image.Image:
    """
    Receives an RGBA image (background already removed)
    Returns a cropped image containing only the largest connected subject.
    """

    # Ensure image is in RGBA mode
    if image.mode != "RGBA":
        image = image.convert("RGBA")
    
    # Convert image to numpy array
    img_np = np.array(image)

    # Create a binary mask where alpha channel > 0 (identify objects' pixels)
    alpha = img_np[:, :, 3]

    mask = alpha > 0

    # Label connected components (objects) in the mask
    labeled, num_objects = label(mask)


    if num_objects == 0:
        raise ValueError("No subject found in the image")
    
    # find the largest connected component
    areas = []
    for i in range(1, num_objects + 1):
        area = np.sum(labeled == i)
        areas.append(area)
    
    largest_object = np.argmax(areas) + 1

    # Create a mask for the largest object
    ys, xs = np.where(labeled == largest_object)

    min_x, max_x = xs.min(), xs.max()
    min_y, max_y = ys.min(), ys.max()

    # Crop the image to the bounding box of the largest object 
    cropped_image = image.crop((min_x, min_y, max_x + 1, max_y + 1))
    
    return cropped_image
