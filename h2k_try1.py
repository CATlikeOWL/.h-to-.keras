import os

# 查看當前工作目錄
cwd = os.getcwd()
print("目前位置:", cwd)
print("目前目錄檔案列表:", os.listdir(cwd))

# 轉檔程式：將舊模型存成新版可用的 .keras 格式
import tensorflow as tf
from tensorflow.keras.models import load_model
print(tf.__version__)  # 應該是 2.12.0

# Step 0: 載入舊模型
old_model_path = "model105QQ_2_f2"  # 你的舊檔案路徑
model = load_model(old_model_path)

# Step 1: 建立 output 資料夾（如果還沒存在）
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Step 2: 存成 Keras v3 推薦的 .keras 格式
#new_model_path = "model105QQ_2_f2_converted.keras"
model_filename = "model105QQ_2_f2_converted.keras"
new_model_path = os.path.join(output_dir, model_filename)

model.save(new_model_path, save_format="keras")

print(f"OK~ 模型已轉存完成: {new_model_path}")

#git add output/model105QQ_2_f2_converted.keras
#git commit -m "Add converted model to output folder"
#git push
