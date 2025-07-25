
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
df = pd.read_csv("employee_salary_dataset (1).csv")

# Features and target
X = df[['Experience', 'Education', 'JobRole']]
y = df['Salary']

# Preprocessing (one-hot encoding for categorical variables)
categorical_features = ['Education', 'JobRole']
preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(drop='first'), categorical_features)
], remainder='passthrough')

# Create pipeline with preprocessing + Linear Regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(y_pred[0])

print(f'R² Score: {r2:.3f}')
print(f'Mean Absolute Error: {mae:.2f}')
