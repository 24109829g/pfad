import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'C:/Users/Administrator/PycharmProjects/pfad/assignment_tao/marine-recent-en.csv'
df = pd.read_csv(file_path)

# Convert '5-day Biochemical Oxygen Demand (mg/L)' to numeric, coerce errors to NaN
df['5-day Biochemical Oxygen Demand (mg/L)'] = pd.to_numeric(df['5-day Biochemical Oxygen Demand (mg/L)'], errors='coerce')

# Convert 'Sampling Date (MM/YYYY)' to datetime
df['Sampling Date'] = pd.to_datetime(df['Sampling Date (MM/YYYY)'], format='%m/%Y')

# Set seaborn style
sns.set(style="whitegrid")

# Plot Dissolved Oxygen levels over time, grouped by Water Control Zone
plt.figure(figsize=(12, 6))
sns.lineplot(x='Sampling Date', y='Dissolved Oxygen (mg/L)', hue='Water Control Zone', data=df, marker='o')

# Customize the plot
plt.title('Dissolved Oxygen Levels Over Time by Water Control Zone', fontsize=14)
plt.xlabel('Sampling Date', fontsize=12)
plt.ylabel('Dissolved Oxygen (mg/L)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Water Control Zone', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show plot
plt.show()
