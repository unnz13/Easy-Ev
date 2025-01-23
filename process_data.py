import pandas as pd

# 更改为你的CSV文件的完整路径
file_path = '/Users/sangruoxuan/Downloads/NumStation+AADT/NumStation+AADT.csv'

# 加载CSV文件
data = pd.read_csv(file_path)

# 将所有可能的列转换为数值类型
data = data.apply(pd.to_numeric, errors='coerce')

# 填充NaN值为0
data.fillna(0, inplace=True)

# 保存处理后的数据到新的CSV文件
processed_file_path = '/Users/sangruoxuan/Downloads/NumStation+AADT/processed_data.csv'
data.to_csv(processed_file_path, index=False)

print(f"Processed data saved to {processed_file_path}")