from flask import Flask, render_template, request

app = Flask(__name__)

# load the model
import pickle
with open('iris_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get input data from the form
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])

    # make predictions using the loaded model
    input_data = [[petal_length, petal_width, sepal_length, sepal_width]]
    prediction = model.predict(input_data)

    # return the predicted class
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)