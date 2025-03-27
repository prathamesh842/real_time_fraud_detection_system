from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open(r"C:\Users\PRATHAMESH\Desktop\Real time Credit Card dETECTION\notebooks\fraud_detection.pkl", 'rb') as f:
    model = pickle.load(f)

# Route to serve the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']

    # Make a prediction
    prediction = model.predict([features])
    fraud_probability = model.predict_proba([features])[0][1]

    return jsonify({
        'prediction': int(prediction[0]),
        'fraud_probability': float(fraud_probability)
    })

if __name__ == '__main__':
    app.run(debug=True)