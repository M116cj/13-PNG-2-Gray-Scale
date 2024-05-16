from PIL import Image
import pandas as pd

# 讀取PNG圖像
image = Image.open("record_1.png")

# 將圖像轉換為灰度
image = image.convert("L")

# 將圖像轉換為數據框
data = pd.DataFrame(list(image.getdata()))

# 設置列名稱
data.columns = ["pixel_value"]

# 將數據框儲存為CSV檔案
data.to_csv("image_data.csv", index=False)
