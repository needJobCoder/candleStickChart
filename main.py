import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
csv = pd.read_csv('/home/needjobcoder/devlopment/python/dataSciencePractice/practice/stockMarket/archive/ADANIPORTS.csv')
csv['Date'] = pd.to_datetime(csv['Date'])

# Extract dates and volumes
dates = csv['Date']
volumes = csv['Volume']

# Convert 'Volume' to a NumPy array
volumes_array = volumes.values

# Create a bar plot
fig, ax = plt.subplots()
ax.bar(dates, volumes_array, width=1, edgecolor="black", linewidth=1)

# Set x-axis and y-axis limits
ax.set_xlim(dates.iloc[0], dates.iloc[-1])
ax.set_ylim(0, volumes_array.max())

# Set labels and title
ax.set(xlabel='Date', ylabel='Volume', title='Adani Port Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.savefig('output_plot.png')

