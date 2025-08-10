import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the data
df = pd.read_csv('/Users/nasimattar/Documents/Uni/People_analytics/fau_clinic_recruitment.csv')

# Drop irrelevant columns
relevant_data = df.drop(columns=['gender', 'location', 'hired', 'family_nurse', 'occupational_health_nursing', 'gerontological_nursing'])

# Convert 'experience' column into bins
relevant_data['experience'] = pd.cut(relevant_data['experience'], bins=[0, 5, 10, 15, float('inf')], labels=['0-5', '5-10', '10-15', '15+'], right=False)

# One-hot encode the categorical columns
relevant_data_encoded = pd.get_dummies(relevant_data, columns=['experience', 'education', 'field'])

# Apply apriori algorithm to find frequent itemsets with support >= 0.02
frequent_itemsets = apriori(relevant_data_encoded, min_support=0.02, use_colnames=True)
num_itemsets = frequent_itemsets.shape[0]

# Generate association rules
rules = association_rules(frequent_itemsets,num_itemsets=num_itemsets, metric="confidence", min_threshold=0.25)

# Sort rules by lift in descending order
sorted_rules = rules.sort_values(by=['lift'], ascending=False)

# Select only antecedents, consequents, support, confidence, and lift
selected_columns = sorted_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

# Print the selected columns to the terminal
print(selected_columns.to_string())  # Ensures full DataFrame is displayed without truncation

# Save the selected columns to a CSV file
output_file = '/Users/nasimattar/Documents/Uni/People_analytics/all_antecedents_association_rules.csv'
selected_columns.to_csv(output_file, index=False)

print(f"\nAll antecedents and association rules saved to {output_file}")