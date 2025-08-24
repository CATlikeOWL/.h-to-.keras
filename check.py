from tensorflow.keras.models import load_model

test_model = load_model("output/model105QQ_2_f2_converted.keras")
test_model.summary()  # 顯示模型架構

# 選擇你想看的層（可以用 index 或 name）
layer_index = 0  # 也可以用 model.get_layer('layer_name') 找

layer = test_model.layers[layer_index]

# 取得該層的參數（權重和偏差）
weights = layer.get_weights()

print(f"第 {layer_index} 層 ({layer.name}) 的參數數量:", len(weights))

for i, w in enumerate(weights):
    print(f"")
    print(f"參數 {i} 的形狀:", w.shape)
    print(f"參數 {i} 的前10個值:", w.flatten()[:10]*2**9)
    print(f"")

#修改保存到遠端（GitHub）
'''
git add *.py           # 把所有.py檔案加入暫存區
git commit -m "Save all python files"
git push               # 推送到遠端分支
'''