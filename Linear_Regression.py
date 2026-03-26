import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# 1. Load CSV
df = pd.read_csv(r"")
# replace with your own csv file path after r

# 2. Remove rows with NULL values in selected columns
columns_to_check = [
    "Garden_Points",
    "Estimate_the_amount_of_tree_canopy__shade__on_your_property_from",
    "What_portion_of_surrounding_lands_have_habitat__e_g__gardens__tr",
    "Size_and_Habitat"
]

df = df.dropna(subset=columns_to_check)

# 3. Select predictors (X) and target (y)
X = df[[ 
    "Garden_Points",
    "Estimate_the_amount_of_tree_canopy__shade__on_your_property_from",
    "What_portion_of_surrounding_lands_have_habitat__e_g__gardens__tr"
]]

y = df["Size_and_Habitat"]

# 4. Z-SCORE STANDARDIZE predictors
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 6. Regression model
model = LinearRegression()
model.fit(X_train, y_train)


# 7. Standardized coefficients
print("\nSTANDARDIZED COEFFICIENTS (Z-score):")
for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef}")

print("\nINTERCEPT (not standardized):", model.intercept_)

# 8. Model performance
y_pred = model.predict(X_test)
print("\nR² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# 9. Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Size_and_Habitat")
plt.ylabel("Predicted Size_and_Habitat")
plt.title("Actual vs Predicted Size_and_Habitat (Z-Score Standardized Predictors)")
plt.show()
