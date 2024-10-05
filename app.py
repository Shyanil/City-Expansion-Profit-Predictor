from flask import Flask, request, jsonify
from model_params import w, b  # Import w and b from the model_params.py file

app = Flask(__name__)

# Function to predict profit
def predict_and_prin(population, w, b):
    predicted_profit = (w * (population / 10000) + b) * 10000
    return {
        'message': f'For a city with a population of {population:,}, the estimated annual profit is ${predicted_profit:,.2f}.',
        'population': population,
        'estimated_profit': f"${predicted_profit:,.2f}",
        'note': 'This is an estimate based on population size and other model parameters.'
    }

# API Route to predict profit based on population
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if 'population' not in data:
        return jsonify({'error': 'Please provide a population value'}), 400

    try:
        population = int(data['population'])
        result = predict_and_prin(population, w, b)
        return jsonify(result), 200
    except ValueError:
        return jsonify({'error': 'Invalid population value. Please provide a number.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
