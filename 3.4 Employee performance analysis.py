# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, r2_score, classification_report

# Load Dataset
file_path = '/Users/nasimattar/Documents/Uni/People_analytics/clinic_performance.csv'
df = pd.read_csv(file_path)

# Inspect the data
print("Dataset Overview:")
print(df.info())
print(df.describe())
print("Columns:", df.columns)
print("Any Missing Values:", df.isnull().values.any())

# Visualize Performance Distribution
sns.histplot(df['PerformanceRating'], bins=10, color='blue', kde=False, edgecolor='black')
plt.title('Histogram of Employee Performance Ratings')
plt.xlabel('Performance Rating')
plt.ylabel('Count')
plt.show()

# Prepare Data for Analysis
# Exclude EmpNumber and perform label encoding for categorical features
categorical_features = ["Gender", "MaritalStatus", "EmpJobRole", "OverTime", "Attrition"]
X = df.drop(columns=["EmpNumber", "PerformanceRating"])  # Features
y = df["PerformanceRating"]  # Target

# Apply Label Encoding to categorical columns
le = LabelEncoder()
for feature in categorical_features:
    X[feature] = le.fit_transform(X[feature])

# Calculate and visualize correlation matrix
correlation_matrix = X.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()

# Feature Correlation with Target
data = pd.get_dummies(df, drop_first=True)
X_corr = data.drop(columns=['PerformanceRating'])
y_corr = data['PerformanceRating']
correlation_scores = X_corr.apply(lambda feature: feature.corr(y_corr))
feature_corr_df = pd.DataFrame({
    'Feature': correlation_scores.index,
    'Correlation_Score': correlation_scores.values,
    'Abs_Correlation_Score': correlation_scores.abs()
}).sort_values(by='Abs_Correlation_Score', ascending=False)

print("\nTop Features by Correlation with PerformanceRating:")
print(feature_corr_df.head(5))  # Adjust the number for more features if needed

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=32)

# Train Gradient Boosting Classifier
gbm_model = GradientBoostingClassifier(random_state=42)
gbm_model.fit(X_train, y_train)

# Make Predictions and Evaluate
y_pred = gbm_model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

# R2 Score
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)

# Classification Report
class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)
feature_corr_df.to_csv('feature_correlations.csv', index=False)
print("Feature correlations saved to 'feature_correlations.csv'")
