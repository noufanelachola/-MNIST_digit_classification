
# Step 1: Load & Preprocess Data (Flatten & Normalize)
# Step 2: Train Different ML Models
    # Logistic Regression (Baseline)
    # SVM (Support Vector Machine) (Stronger Model)
    # Random Forest (Tree-Based Approach)   
    # KNN (K-Nearest Neighbors) (Alternative)
# Step 3: Compare Model Performance
# Step 4: Hyperparameter Tuning for Best Accuracy
# Step 5: Final Model Selection & Testing on Unseen Data

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

# Flatten the images
X_train = X_train.reshape(60000,784)
X_test = X_test.reshape(10000,784)

# Normalise the data
X_train = X_train/255
X_test = X_test/255

# Split the training data
X_train,X_val,y_train,y_val = train_test_split(X_train,y_train,test_size=0.2,random_state=42)


# Logistic regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train,y_train)

y_pred = logistic_model.predict(X_val)
accuracy = accuracy_score(y_pred,y_val)

print(f"Accuracy Score : {accuracy}")

# Show the image
plt.imshow(X_train[0].reshape(28,28), cmap="gray")
plt.title(f"{y_train[0]}")
plt.show()