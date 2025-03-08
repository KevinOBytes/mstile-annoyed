from pathlib import Path
from typing import Tuple, List
from PIL import Image

MSTILE_SIZES = [
    (70, 70),
    (144, 144),
    (150, 150),
    (310, 310),
    (310, 150)
]

def resize_image(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Resize an image to the specified size while maintaining aspect ratio and adding padding if necessary.
    
    Args:
        image: PIL Image object
        size: Target size as (width, height)
    
    Returns:
        Resized PIL Image object
    """
    # Create a new image with transparent background
    new_image = Image.new('RGBA', size, (0, 0, 0, 0))
    
    # Calculate scaling factor to fit within the target size
    scale_w = size[0] / image.width
    scale_h = size[1] / image.height
    scale = min(scale_w, scale_h)
    
    # Calculate new dimensions
    new_w = int(image.width * scale)
    new_h = int(image.height * scale)
    
    # Resize the original image
    resized = image.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Calculate position to center the image
    x = (size[0] - new_w) // 2
    y = (size[1] - new_h) // 2
    
    # Paste the resized image onto the new background, using alpha channel as mask
    new_image.paste(resized, (x, y), resized)
    
    return new_image

def generate_mstile_icons(input_path: str, output_dir: str) -> List[str]:
    """
    Generate mstile icons from an input image.
    
    Args:
        input_path: Path to the input image
        output_dir: Directory to save the generated icons
    
    Returns:
        List of generated icon paths
    """
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Open and convert input image to RGBA
    with Image.open(input_path) as img:
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        generated_files = []
        
        # Generate icons for each size
        for width, height in MSTILE_SIZES:
            output_file = output_path / f"mstile-{width}x{height}.png"
            resized = resize_image(img, (width, height))
            resized.save(output_file, "PNG")
            generated_files.append(str(output_file))
    
    return generated_files 