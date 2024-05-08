import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example data
data = np.array([
    [85, 85, 1],
    [80, 70, 1],
    [68, 65, 0],
    [90, 90, 1],
    [55, 60, 0],
    [60, 65, 0]
])

# Split into features and target
X = data[:, :2]  # all rows, first two columns
y = data[:, 2]   # all rows, third column

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
