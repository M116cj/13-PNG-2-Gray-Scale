from PIL import ImageGrab
import time

# 設置屏幕截取區域和錄製時間
x, y, w, h = 219, 213, 500, 139
duration = 5  # 每個迴圈的錄製時間
record_count = 1  # 要錄製的次數

# 開始錄製
count = 1
while count <= record_count:
    # 截取屏幕圖像
    im = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    
    # 將圖像保存為新的 PNG 文件
    filename = f"record_{count}.png"
    im.save(filename)
    
    # 等待指定的時間
    time.sleep(duration)
    
    count += 1
