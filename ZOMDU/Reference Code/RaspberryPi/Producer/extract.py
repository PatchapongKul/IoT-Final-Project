import pandas as pd
import numpy as np

# Assuming df is your DataFrame containing the dataset
df = pd.read_csv('Occupancy_Estimation.csv')
# Separate the dataset into different classes based on Room_Occupancy_Count
classes = df['Room_Occupancy_Count'].unique()

# Initialize empty lists to store training and test samples
train_samples = []
test_samples = []

# Randomly select 100 samples per class for the training set
for c in classes:
    class_samples = df[df['Room_Occupancy_Count'] == c]
    selected_samples = class_samples.sample(n=100, random_state=42)  # You can change the random_state for different random selection
    train_samples.append(selected_samples)
    # Exclude selected samples from the dataset to create the test set
    test_samples.append(class_samples.drop(selected_samples.index))

# Concatenate the selected samples for each class to create the training and test sets
train_set = pd.concat(train_samples)
test_set = pd.concat(test_samples)

# Shuffle the training and test sets
train_set = train_set.sample(frac=1, random_state=42).reset_index(drop=True)
test_set = test_set.sample(frac=1, random_state=42).reset_index(drop=True)

# Sort train_set by the 'Room_Occupancy_Count' column
train_set_sorted = train_set.sort_values(by='Room_Occupancy_Count')

# Save the sorted train_set to a CSV file
train_set_sorted.to_csv('test_cases.csv', index=False)
test_set.to_csv('train_set.csv', index=False)
