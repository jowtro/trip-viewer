import pandas as pd

# Specify the path to your JSON Lines file
file_path = 'mock_test.txt'

# Load JSON Lines data from file into a pandas DataFrame
df = pd.read_json(file_path, lines=True)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Calculate metrics
engine_running_time = df[df['engine'].apply(lambda x: x.get('status', '') == 'running')]['engine'].count()
engine_off_time = df[df['engine'].apply(lambda x: x.get('status', '') == 'off')]['engine'].count()

# Check if 'odometer' key exists before calculating total distance
if 'odometer' in df.columns and 'value' in df['odometer'].apply(lambda x: x.get('value') if pd.notna(x) else None).dropna().tolist():
    total_distance = df['odometer'].apply(lambda x: x.get('value') if pd.notna(x) else None).dropna().max() - df['odometer'].apply(lambda x: x.get('value') if pd.notna(x) else None).dropna().min()
else:
    total_distance = 0

average_speed = df['speed'].apply(lambda x: x.get('value') if pd.notna(x) else None).dropna().mean()


# EXAMPLES
# Display metrics
print("\nMetrics:")
print(f"Engine Running Time: {engine_running_time} entries")
print(f"Engine Off Time: {engine_off_time} entries")
print(f"Total Distance: {total_distance} km")
print(f"Average Speed: {average_speed} km/h")
