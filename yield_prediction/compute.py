import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# 读取 CSV 文件
df = pd.read_csv('./output/yield_prediction_output.csv')

# 提取 YIELD 和 prediction 列
YIELD = df['YIELD'] * 100
prediction = df['prediction']

# 计算 RMSE
rmse = np.sqrt(mean_squared_error(YIELD, prediction))

# 计算 R² score
r2 = r2_score(YIELD, prediction)

print(f"RMSE: {rmse}")
print(f"R² score: {r2}")