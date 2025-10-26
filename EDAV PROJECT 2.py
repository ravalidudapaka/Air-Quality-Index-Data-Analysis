#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\RANI\\Downloads\\data_date (1).csv")

# Print columns to verify
print("Columns in dataset:", df.columns)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Fill missing values
df["Country"].fillna("Unknown", inplace=True)   # categorical
df["Status"].fillna("Unknown", inplace=True)    # categorical
df["AQI Value"].fillna(df["AQI Value"].mean(), inplace=True)  # numeric

print(" Q1: Mean and Max AQI by Status")
aqi_stats = df.groupby("Status")["AQI Value"].agg(["mean", "max"])
print("\nMean and Max AQI by Status:")
print(aqi_stats)

print("Q2: Average AQI by Country")
country_avg = df.groupby("Country")["AQI Value"].mean()
print("\nAverage AQI by Country:")
print(country_avg)

print("Q3: Line chart for AQI trend by Status")
plt.figure(figsize=(10,6))
for status in df["Status"].unique():
    status_data = df[df["Status"] == status]
    plt.plot(status_data["Date"], status_data["AQI Value"], label=status)

plt.title("AQI Trend Over Time by Status")
plt.xlabel("Date")
plt.ylabel("AQI Value")
plt.legend()
plt.show()

print("Q4: Correlation between numeric columns")
numeric_cols = ["AQI Value"]
corr = df[numeric_cols].corr()
print("\nCorrelation between numeric columns:")
print(corr)

print("Q5: Status with highest mean AQI")
highest_status = aqi_stats["mean"].idxmax()
print("\nStatus with highest average AQI:", highest_status)


# In[ ]:






# In[ ]:





# In[ ]:




