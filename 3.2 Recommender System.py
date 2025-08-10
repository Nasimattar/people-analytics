import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
file_path = '/Users/nasimattar/Documents/Uni/People_analytics/fau_clinic_recommender_system.csv'
fau_clinic_data = pd.read_csv(file_path)

# Combine relevant features into a single column
fau_clinic_data['combined_features'] = fau_clinic_data['teams'] + ' ' + \
                                       fau_clinic_data['hobbies'] + ' ' + \
                                       fau_clinic_data['sports']

# Convert the combined features into TF-IDF vectors
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(fau_clinic_data['combined_features'])

# Identify the row index of the new employee (e.g., emp_050)
new_employee_index = fau_clinic_data[fau_clinic_data['id'] == 'emp_050'].index[0]

# Compute the cosine similarity scores for the new employee against all others
similarity_scores = cosine_similarity(tfidf_matrix[new_employee_index], tfidf_matrix)
similarity_scores_list = similarity_scores[0]

# Add the similarity scores as a new column in the dataframe
fau_clinic_data['similarity_score'] = similarity_scores_list

# Sort by similarity score in descending order
fau_clinic_data_sorted = fau_clinic_data.sort_values(by='similarity_score', ascending=False)

# Display the dataset with the similarity scores
print(fau_clinic_data_sorted[['id', 'teams', 'hobbies', 'sports', 'similarity_score']])

# Extract the top 3 most similar employees (excluding the new hire)
top_similar_employees = fau_clinic_data_sorted[fau_clinic_data_sorted['id'] != 'emp_050'].head(3)
print("\nTop 3 most similar employees:")
print(top_similar_employees[['id', 'teams', 'hobbies', 'sports', 'similarity_score']])