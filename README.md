# GIS-Based Linear Regression Analysis (Python)

This project applies a linear regression model to analyze relationships between ecological variables and a composite site index using Python.

## Overview
The goal of this project is to understand how environmental factors such as vegetation, canopy cover, and surrounding habitat contribute to overall landscape health.

## Features
- Data cleaning and preprocessing (handling missing values)
- Feature standardization using Z-score normalization
- Linear regression modeling using scikit-learn
- Model evaluation using R² and Mean Squared Error (MSE)
- Visualization of actual vs predicted values

## Variables
**Predictors (X):**
- Garden Points (site-level ecological score)
- Tree Canopy Coverage
- Surrounding Habitat Proportion

**Target (y):**
- Size and Habitat Index (composite environmental indicator)

## Tools & Technologies
- Python
- Pandas
- Scikit-learn
- Matplotlib

## Workflow
1. Load dataset from CSV
2. Remove missing values
3. Select predictor and target variables
4. Standardize predictors (Z-score)
5. Split data into training and testing sets
6. Train linear regression model
7. Evaluate model performance (R², MSE)
8. Visualize predicted vs actual results

## Results
The model outputs standardized coefficients, allowing comparison of the relative importance of each environmental variable.

## Use Case
This analysis can support environmental planning and decision-making by identifying key factors that influence ecological health.

## Notes
- Dataset is not included for privacy reasons
- Replace the CSV path with your own dataset when running the code

## Author
Enran Zu
