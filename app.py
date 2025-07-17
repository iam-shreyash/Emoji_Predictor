
from flask import Flask, render_template, request, jsonify
import model  # Make sure model.py is in same folder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input = data['text']
    prediction = model.predict_emoji(user_input)
    return jsonify({'emoji': prediction})

if __name__ == '__main__':
    app.run(debug=True)
