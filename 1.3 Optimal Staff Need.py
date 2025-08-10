import pandas as pd

# Load the dataset
file_path = '/Users/nasimattar/Documents/Uni/People_analytics/fau_medical_staff.csv'
data = pd.read_csv(file_path)

# Create a new column to identify which shift each row belongs to
data['Shift'] = data[['Shift 1', 'Shift 2', 'Shift 3']].apply(lambda row: row.first_valid_index(), axis=1)

# Calculate the total average patients for each shift
shift_totals = data.groupby('Shift')['Avg_Patient_Number'].sum()

# Calculate the number of medical assistants needed per shift
assistants_needed = (shift_totals / 4).apply(lambda x: int(x) if x == int(x) else int(x) + 1)

# Combine the results into a summary DataFrame
results = pd.DataFrame({
    'Total_Patients': shift_totals,
    'Medical_Assistants_Required': assistants_needed
})

# Display the results
print(results)