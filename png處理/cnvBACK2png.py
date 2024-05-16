import csv
import numpy as np
from PIL import Image

def csv_to_png(csv_file, output_file):
    # 讀取CSV檔案
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # 將數據轉換為NumPy數組
    img_data = np.array(data, dtype=np.uint8)

    # 使用PIL將數組保存為PNG圖像
    img = Image.fromarray(img_data, "L")  # "L"代表灰度圖像
    img.save(output_file)

# 使用範例
csv_file = "E:\Code_代碼\image_data.csv"
output_file = "output_image.png"
csv_to_png(csv_file, output_file)
