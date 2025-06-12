import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import missingno as msno
from scipy.stats import shapiro


# Connect to MySQL and accessing the car Database created inside the MYSQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jobin1995",
    database="car"
)

cursor = conn.cursor()


#Load entire table car_ds into pandas Dataframe
cursor.execute("SELECT * FROM car_ds")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])


print("\n=== Data Info ===")
print(df.info())

print("\n=== Missing Values ===")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

print("\n==Missing values per column(feature)==")
df.isna().mean().sort_values().plot(
    kind="bar", figsize=(15, 4),
    title="Percentage of missing values per feature",
    ylabel="Ratio of missing values per feature");

print("\n==Removing features which is having more than 40percent missing values")
df = df.dropna(thresh=df.shape[0] *0.60, axis=1)
df.shape
print(df.shape)

print("\n=== Summary Statistics ===")
print(df.describe())


print("\n== categorical variables and numerical variables")
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
num_categorical = len(categorical_cols)



print(f"Categorical columns ({num_categorical}): {categorical_cols}")


numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
num_data=len(numerical_cols)

print(f"numerical_cols ( {num_data}):  {numerical_cols}")



# Distribution plots for variables


print("\n=== Distribution Plots for numerical  ===")
num_cols = numerical_cols

n_cols = 3
n_rows = math.ceil(len(num_cols) / n_cols)
plt.figure(figsize=(n_cols * 5, n_rows * 4))

for i, col in enumerate(num_cols, 1):
    plt.subplot(n_rows, n_cols, i)
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

print("\n==Distribution plots  categorical  ===")
categorical_cols = df.select_dtypes(include='object').columns[:10]

# Set up the subplot grid
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
axes = axes.flatten()  # flatten 2D grid to 1D array for easy indexing

# Loop over 10 categorical columns
for i, col in enumerate(categorical_cols):
    sns.countplot(data=df, y=col, ax=axes[i], order=df[col].value_counts().index[:10])
    axes[i].set_title(col)
    axes[i].set_xlabel('Count')
    axes[i].set_ylabel('')

# Adjust layout
plt.tight_layout()
plt.suptitle("Distribution of 10 Categorical Variables", fontsize=16, y=1.03)
plt.show()




print("\n=== most frequent entry or Over represented feature value==")
# Step 1: Get the most frequent value (mode) for each column
most_frequent_entry = df.mode().iloc[0]  # Only use the first mode if multiple exist

# Step 2: Create a boolean DataFrame where each cell is True if it equals the mode
df_freq = df.eq(most_frequent_entry, axis=1)

# Step 3: Compute the ratio of most frequent entries per column
freq_ratio = df_freq.mean().sort_values(ascending=False)

# Step 4: (Optional) Exclude numerical columns if desired
categorical_cols = df.select_dtypes(include='object').columns
freq_ratio = freq_ratio[freq_ratio.index.isin(categorical_cols)]

# Step 5: Get Top 20 columns with highest frequency ratio
top_20 = freq_ratio.head(20)
print("Top 20 columns with highest single-value dominance:\n", top_20)

# Step 6: Plot
plt.figure(figsize=(10, 5))
top_20.plot(kind='bar', color='salmon')
plt.title('Top 20 Columns with Highest Most Frequent Value Ratio')
plt.ylabel('Frequency Ratio')
plt.xlabel('Feature')
plt.xticks(rotation=90)
plt.ylim(0, 1.0)
plt.tight_layout()
plt.show()

print("\n=== graph on features with less missing values==")

# Step 1: Count missing values per column
missing_counts = df.isnull().sum()

# Step 2: Filter categorical columns with <10% missing values AND at least 4 unique values
categorical_cols = df.select_dtypes(include='object').columns
low_missing_cats = [
    col for col in categorical_cols
    if missing_counts[col] < len(df) * 0.1 and df[col].nunique(dropna=True) >= 4
]
print(low_missing_cats)
# Step 3: Plot top 10 most frequent values in each selected column
for col in low_missing_cats:
    top_values = df[col].value_counts().head(10)
    print(f"\nTop values in column: {col}")
    print(top_values)

    plt.figure(figsize=(8, 4))
    sns.barplot(x=top_values.values, y=top_values.index, hue=top_values.index, legend=False, palette="viridis")
    plt.title(f"Top Most Frequent Values in '{col}' (Low Missing & ≥4 Unique)")
    plt.xlabel("Count")
    plt.ylabel(col)
    plt.tight_layout()
    plt.show()




# FEATURE RELATIONSHIPS

 #  For checking relationships between the numerical variables     
df_corr = df.select_dtypes(include=['number']).corr(method="pearson")


plt.figure(figsize=(12, 8))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


        
      
#NORMALITY TEST(Shapiro-Wilk test)

for col in numerical_cols:
    try:
        stat, p_value = shapiro(df[col].dropna())  # Drop NA to avoid errors
        print(f"Shapiro-Wilk test for {col}: p = {p_value:.4f}")
        if p_value > 0.05:
            print(" -> Likely normal")
        else:
            print(" -> Not normal")
    except Exception as e:
        print(f"Could not perform Shapiro-Wilk test for {col}: {e}")




conn.close()
