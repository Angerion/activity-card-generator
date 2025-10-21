from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image(text, filename, size=(400, 400), bg_color=(100, 150, 200)):
    """Create a simple test image with text"""
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)
    
    # Draw text
    draw.text(position, text, fill=(255, 255, 255), font=font)
    
    img.save(filename)
    print(f"Created: {filename}")

# Create test images with different counts
create_test_image("Swim", "koupání_12.png", bg_color=(65, 105, 225))
create_test_image("Run", "běhání_6.png", bg_color=(220, 20, 60))
create_test_image("Jump", "skákání_8.png", bg_color=(50, 205, 50))
create_test_image("Read", "čtení_4.png", bg_color=(255, 140, 0))

print("\nTest images created successfully!")
