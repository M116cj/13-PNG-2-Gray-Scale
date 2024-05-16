from PIL import Image

def get_image_size(file_path):
    img = Image.open(file_path)
    return img.size

image_path = 'E:\Code_代碼\record_1.png'
width, height = get_image_size(image_path)
print(f"Image dimensions (width, height): ({width}, {height})")
