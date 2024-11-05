# highSeas-spagethi


# 🍝 Virtual Spaghetti Painter

A fun Python project that splatters virtual pasta shapes (spaghetti, ravioli, etc.) over a user-uploaded photo! This project uses random shapes and colors to simulate a whimsical "spaghetti splash" effect.

## 📜 Project Overview
The Virtual Spaghetti Painter is a simple Python-based image manipulation tool that:
- Loads a user-uploaded image.
- Adds random pasta-shaped overlays like circles and lines (representing spaghetti and other pasta types).
- Outputs a fun, pasta-splattered version of the original image.

## 📂 Files
- `spaghetti_painter.py`: Main script to apply the pasta splatter effect on an image.
- `README.md`: Project documentation (this file).

## 🚀 Getting Started
### Prerequisites
- **Python 3.6+**
- **Pillow (PIL) Library** for image processing:
  ```bash
  pip install pillow
  ```

### Usage
1. **Save your image** in the same directory as the project or note its path.
2. **Run the script** with your image path:
   ```bash
   python spaghetti_painter.py
   ```

3. **Customize the output**:
   - Adjust the number of splatters or colors if desired.
   - The output will be saved as `spaghetti_painter_output.png` by default.

### Example
```python
image_path = "user_photo.jpg"  # Replace with your image path
output_path = "spaghetti_painter_output.png"
main(image_path, output_path)
```

## 📝 Code Overview
- **`load_image(image_path)`**: Loads the image and prepares it for pasta overlays.
- **`create_pasta_splatter(img, splatter_count=100)`**: Draws random pasta shapes (circles and lines) in varying sizes and colors on a transparent layer and combines it with the original image.
- **`main(image_path, output_path="spaghetti_painter_output.png")`**: Main function that loads the image, applies the pasta splatter effect, and saves the output.

## 🎨 Customization
You can customize:
- **`splatter_count`**: Number of pasta splatters (default is 100).
- **Pasta Colors**: Modify `pasta_colors` in `create_pasta_splatter` to add different shades.
- **Shape Types**: Experiment with shapes and sizes to create different pasta looks!


## 🛠️ Future Improvements
- Add more pasta types (shells, spirals, etc.)
- Allow for more user control over shape colors, sizes, and densities.
- Support different background textures or patterns.

## 📜 License
This project is open-source and free to use.
