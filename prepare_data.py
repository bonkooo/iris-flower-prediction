import pandas as pd
from sklearn.model_selection import train_test_split

# load the dataset
df = pd.read_csv('iris.csv')

# split the data into features (X) and labels (y)
X = df.drop('species', axis=1)
y = df['species']

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# saving preprocessed data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)