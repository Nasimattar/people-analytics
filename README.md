# People Analytics Project

A comprehensive Python-based analytics suite for healthcare workforce management, recruitment optimization, employee matching, and performance analysis.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Requirements](#data-requirements)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## 🎯 Overview

This project provides data-driven solutions for human resources management in healthcare settings, focusing on four key areas:
1. **Staff Optimization** - Determining optimal staffing levels
2. **Data-Driven Recruitment** - Finding recruitment patterns using market basket analysis
3. **Employee Matching** - Recommender system for team compatibility
4. **Performance Analysis** - Predictive modeling for employee performance

## 📁 Project Structure

```
People Analytics/
├── 1.3 Optimal Staff Need.py          # Staff optimization calculator
├── 2.2 Data driven recruitment.py     # Recruitment pattern analysis
├── 3.2 Recommender System.py          # Employee matching system
├── 3.4 Employee performance analysis.py # Performance prediction model
└── README.md                          # Project documentation
```

## ✨ Features

### 1. Optimal Staff Need Analysis (`1.3 Optimal Staff Need.py`)
- **Purpose**: Calculate required medical assistants per shift based on patient load
- **Methodology**: Analyzes patient distribution across shifts and applies staffing ratios
- **Key Features**:
  - Processes multi-shift patient data
  - Calculates staff requirements with 1:4 patient-to-assistant ratio
  - Provides shift-wise staffing recommendations

### 2. Data-Driven Recruitment (`2.2 Data driven recruitment.py`)
- **Purpose**: Discover recruitment patterns using association rule mining
- **Methodology**: Market basket analysis with Apriori algorithm
- **Key Features**:
  - Analyzes candidate profiles (experience, education, field)
  - Identifies frequent itemsets and association rules
  - Generates recruitment insights with confidence and lift metrics
  - Exports results for strategic decision making

### 3. Employee Recommender System (`3.2 Recommender System.py`)
- **Purpose**: Match new employees with similar existing team members
- **Methodology**: Content-based filtering using TF-IDF and cosine similarity
- **Key Features**:
  - Analyzes employee profiles (teams, hobbies, sports)
  - Calculates similarity scores between employees
  - Recommends top 3 most compatible colleagues
  - Facilitates team integration and collaboration

### 4. Employee Performance Analysis (`3.4 Employee performance analysis.py`)
- **Purpose**: Predict and analyze employee performance ratings
- **Methodology**: Machine learning with Gradient Boosting Classifier
- **Key Features**:
  - Comprehensive data visualization and exploration
  - Feature correlation analysis
  - Performance prediction modeling
  - Model evaluation with accuracy, R² score, and classification reports
  - Feature importance analysis


## 💻 Usage

### Customizing File Paths

Before running the scripts, update the file paths to match your data location:
- `fau_medical_staff.csv` - Staff scheduling data
- `fau_clinic_recruitment.csv` - Recruitment candidate data  
- `fau_clinic_recommender_system.csv` - Employee profile data
- `clinic_performance.csv` - Performance rating data

## 📊 Data Requirements

### Staff Optimization Data
- Columns: `Shift 1`, `Shift 2`, `Shift 3`, `Avg_Patient_Number`
- Format: CSV with patient counts per shift

### Recruitment Data
- Columns: `experience`, `education`, `field`, `gender`, `location`, `hired`
- Format: CSV with candidate profiles and hiring outcomes

### Recommender System Data  
- Columns: `id`, `teams`, `hobbies`, `sports`
- Format: CSV with employee profile information

### Performance Analysis Data
- Columns: `EmpNumber`, `Gender`, `MaritalStatus`, `EmpJobRole`, `OverTime`, `Attrition`, `PerformanceRating`
- Format: CSV with employee demographics and performance metrics

## 📦 Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **mlxtend**: Association rule mining

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📈 Output Files

The scripts generate the following output files:
- `all_antecedents_association_rules.csv` - Recruitment pattern analysis results
- `feature_correlations.csv` - Performance feature correlation analysis

## 🔗 Repository Information

- **Repository**: people-analytics
- **Owner**: Nasimattar
- **Branch**: main

## 📝 Notes

- Ensure data files are in the correct format and location before running scripts
- Review and adjust minimum support and confidence thresholds in recruitment analysis as needed
- Performance model parameters can be tuned for better accuracy based on your specific dataset
- All scripts include data preprocessing and validation steps

---

*Last Updated: August 10, 2025*