import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# load the preprocessed data
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

# training the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# saving the trained model
with open('iris_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)