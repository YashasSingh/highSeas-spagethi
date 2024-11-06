from PIL import Image, ImageDraw, ImageFilter
import random

def load_image(image_path):
    """
    Load an image from the specified path.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Ensures the image has an alpha channel for overlays
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def create_pasta_splatter(img, splatter_count=100):
    """
    Overlays 'pasta' shapes onto the provided image.
    - img: The background image where the splatters will appear.
    - splatter_count: Number of pasta splatters to generate.
    """
    width, height = img.size
    pasta_overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))  # Transparent layer for pasta shapes
    draw = ImageDraw.Draw(pasta_overlay)
    
    pasta_colors = [(205, 92, 92, 180), (244, 164, 96, 180), (255, 218, 185, 180)]  # Varied pasta tones

    for _ in range(splatter_count):
        # Random position and size for pasta shapes
        x = random.randint(0, width)
        y = random.randint(0, height)
        shape_size = random.randint(10, 30)
        shape_type = random.choice(["circle", "line"])
        
        color = random.choice(pasta_colors)
        
        if shape_type == "circle":
            draw.ellipse([(x, y), (x + shape_size, y + shape_size)], fill=color)
        elif shape_type == "line":
            line_length = random.randint(20, 50)
            line_thickness = random.randint(1, 5)
            angle = random.uniform(0, 360)
            end_x = int(x + line_length * random.uniform(-1, 1))
            end_y = int(y + line_length * random.uniform(-1, 1))
            draw.line((x, y, end_x, end_y), fill=color, width=line_thickness)

    # Merge the pasta splatter overlay with the original image
    combined_img = Image.alpha_composite(img, pasta_overlay)
    return combined_img

def main(image_path, output_path="spaghetti_painter_output.png"):
    # Load image
    img = load_image(image_path)
    if img is None:
        return
    
    # Apply pasta splatter effect
    splattered_img = create_pasta_splatter(img)
    
    # Save the result
    splattered_img.save(output_path)
    splattered_img.show()  # Opens the image in the default image viewer

# Usage
image_path = "Screenshot 2022-11-01 200031.png"  # Replace with your image path
output_path = "spaghetti_painter_output.png"
main(image_path, output_path)
