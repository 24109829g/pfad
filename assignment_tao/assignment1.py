import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
file_path = 'C:/Users/Administrator/PycharmProjects/pfad/assignment_tao/marine-recent-en.csv'
df = pd.read_csv(file_path)

# 转换 '5-day Biochemical Oxygen Demand (mg/L)' 为数值类型，忽略错误
df['5-day Biochemical Oxygen Demand (mg/L)'] = pd.to_numeric(df['5-day Biochemical Oxygen Demand (mg/L)'], errors='coerce')

# 转换 'Sampling Date (MM/YYYY)' 为 datetime 类型
df['Sampling Date'] = pd.to_datetime(df['Sampling Date (MM/YYYY)'], format='%m/%Y')

# 设置 seaborn 风格
sns.set(style="whitegrid")

# 绘制不同水控制区的溶解氧随时间变化的折线图
plt.figure(figsize=(12, 6))
sns.lineplot(x='Sampling Date', y='Dissolved Oxygen (mg/L)', hue='Water Control Zone', data=df, marker='o')

# 定制化图表
plt.title('Dissolved Oxygen Levels Over Time by Water Control Zone', fontsize=14)
plt.xlabel('Sampling Date', fontsize=12)
plt.ylabel('Dissolved Oxygen (mg/L)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Water Control Zone', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 显示图表
plt.show()
