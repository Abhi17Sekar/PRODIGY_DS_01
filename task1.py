# TASK - 1 : AGE GROUP DISTRIBUTION
# visualize the distribution of 15-64 age groups using barchart and histogram across top 10 countries
#------------------------------------------------------------#

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\abhin\OneDrive\Desktop\Prodigy infotech\task 1\API_SP.POP.1564.TO_DS2_en_csv_v2_18948.csv", skiprows=4)
print(df.head())

# Selecting relevant columns and removing null values
Year = '2020'
df_new = df[["Country Name", Year]].dropna()
df_new[Year] = pd.to_numeric(df_new[Year], errors = "coerce")
# select top 10 countries
df_top10 = df_new.nlargest(10, Year)

# Create bar chart
plt.figure(figsize =(12,6))
plt.bar(df_top10['Country Name'], df_top10[Year], color = 'Red', label = '15-64 years')
plt.xlabel('Country')
plt.ylabel('Percentage')
plt.title(f'Distribution of 15-64 Age Group in Top 10 Countries ({Year})')
plt.xticks(rotation=90)
plt.show()
plt.savefig("barchart.png")

# Create a histogram
plt.figure(figsize = (12,6))
sns.histplot(df_top10[Year], bins=10, kde=True, color='blue')
plt.xlabel('Percentage of Population (15-64 years)')
plt.ylabel('Frequency')
plt.title(f'Histogram of 15-64 Age Group Distribution ({Year})')
plt.show()
plt.savefig("Histogram.png")