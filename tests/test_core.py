import os
import pytest
from PIL import Image
from mstile_annoyed.core import resize_image, generate_mstile_icons

@pytest.fixture
def sample_image():
    """Create a sample image for testing."""
    img = Image.new('RGBA', (100, 100), (255, 0, 0, 255))
    return img

def test_resize_image(sample_image):
    """Test that resize_image maintains aspect ratio and centers the image."""
    target_size = (150, 150)
    resized = resize_image(sample_image, target_size)
    
    assert resized.size == target_size
    assert resized.mode == 'RGBA'
    
    # Check if the image is centered (should have transparent pixels on edges)
    edge_pixel = resized.getpixel((0, 0))
    assert edge_pixel[3] == 0  # Alpha channel should be 0 (transparent)
    
    # Check if the original content is preserved in the center
    center_pixel = resized.getpixel((75, 75))
    assert center_pixel == (255, 0, 0, 255)

def test_generate_mstile_icons(tmp_path, sample_image):
    """Test icon generation with all required sizes."""
    # Save sample image to temp directory
    input_path = os.path.join(tmp_path, "input.png")
    sample_image.save(input_path)
    
    # Generate icons
    output_dir = os.path.join(tmp_path, "output")
    generated_files = generate_mstile_icons(input_path, output_dir)
    
    # Check if all required sizes were generated
    expected_sizes = [(70, 70), (144, 144), (150, 150), (310, 310), (310, 150)]
    assert len(generated_files) == len(expected_sizes)
    
    for file_path in generated_files:
        assert os.path.exists(file_path)
        with Image.open(file_path) as img:
            assert img.size in expected_sizes 