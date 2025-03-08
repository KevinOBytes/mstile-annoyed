from PIL import Image
from mstile_annoyed.core import generate_mstile_icons

# Create a test image
test_image = Image.new('RGBA', (512, 512), (255, 0, 0, 255))
test_image.save('test_input.png')

# Generate icons
generated_files = generate_mstile_icons('test_input.png', 'test_output')
print("Generated files:")
for file in generated_files:
    print(f"  - {file}") 