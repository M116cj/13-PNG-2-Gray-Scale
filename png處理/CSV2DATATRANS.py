from PIL import Image
import numpy as np

from PIL import Image
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

# 讀取PNG圖像
image = Image.open("record_1.png")

# 將圖像轉換為NumPy數組
image_array = np.array(image)

# 讀取所有圖像並將它們轉換為NumPy數組
X = []
y = []
for i in range(10):
    image = Image.open(f"record_1.png")
    image_array = np.array(image)
    X.append(image_array)
    y.append(i)

# 將數據分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 將數據展平為一維數組
X_train = np.array(X_train).reshape(len(X_train), -1)
X_test = np.array(X_test).reshape(len(X_test), -1)

# 訓練SVM模型
clf = svm.SVC()
clf.fit(X_train, y_train)

# 在測試集上評估模型
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
