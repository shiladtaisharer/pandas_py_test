import pandas as pd

# Create an example DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Output the entire DataFrame
print("Entire DataFrame:")
print(df)
print("\n")

# Print the first two rows of the DataFrame
print("First two lines:")
print(df.head(2))
print("\n")

# Display information about the DataFrame
print("DataFrame information:")
print(df.info())
print("\n")

# Display DataFrame statistics
print("DataFrame statistics:")
print(df.describe())
