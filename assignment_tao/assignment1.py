import pandas as pd
import matplotlib.pyplot as plt
# Load the data
file_path = 'C:/Users/Administrator/PycharmProjects/pfad/assignment_tao/marine-recent-en.csv'
df= pd.read_csv(file_path)
df=df[df["Station"]=='DM3']
# Convert 'Sampling Date (MM/YYYY)' to datetime
df1= pd.to_datetime(df['Sampling Date (MM/YYYY)'], format='%m/%Y')
# Convert '5-day Biochemical Oxygen Demand (mg/L)' to numeric
df2= pd.to_numeric(df['5-day Biochemical Oxygen Demand (mg/L)'], errors='coerce')
df2.fillna(0,inplace=True)
# Customize the plot
plt.plot(df1,df2,color="red")
plt.title('Dissolved Oxygen Levels Over Time by Deep Bay', fontsize=10)
plt.xlabel('Sampling Date', fontsize=10)
plt.ylabel('Dissolved Oxygen (mg/L)', fontsize=10)
plt.xticks(rotation=45)
# Show plot
plt.show()
