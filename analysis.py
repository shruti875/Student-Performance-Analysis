import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

print(df.head())     #shows first 5 rows 
print(df.info)       #shows columns info

#data understanding
print(df.describe())   #statistics
print(df.columns)      #shows columns names

#basic analysis

print("maths avg:", df['maths marks'].mean())
print("reading avg:", df['reading avg'].mean())
print("writing avg:", df['writing avg'].mean())

#highest and lowest analysis

print("Max Math:", df['maths marks'].max())
print("Min Math:", df['maths marks'].min())

#group analysis by gender

print(df.groupby('gender')['maths marks'].mean())

#test preparation impact

print(df.groupby('test preparation course')['maths marks'].mean())

#visualization

#1.bar chart
sns.barplot(x='gender', y='maths marks', data=df)
plt.title("Average Math Score by Gender")
plt.show()

#2.histogram

sns.histplot(df['maths marks'], bins=10)
plt.title("Distribution of Math Scores")
plt.show()

#3.heatmap

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

#4.boxplot
sns.boxplot(x='gender', y='maths marks', data=df)
plt.show()