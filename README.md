# City Expansion Profit Predictor

**City Expansion Profit Predictor** is an API tool that estimates the annual profit of a city based on its population. Using a linear regression model optimized with gradient descent, this tool provides accurate profit predictions, allowing city planners and decision-makers to make informed choices about expansion and resource allocation.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Predicts annual profit based on city population input.
- Utilizes a linear regression model for accurate predictions.
- Easy-to-use API for integration with other applications.

## Gradient Descent Algorithm

This project employs the **Gradient Descent** algorithm to optimize the linear regression model parameters, enabling precise predictions based on the provided data.

## Technologies Used

- Python
- Flask
- Pandas
- Seaborn
- NumPy

## How It Works

1. The user inputs the population of the city.
2. The application utilizes a linear regression model to calculate the predicted profit.
3. A response is generated, providing the estimated profit along with an informative message.

## API Documentation

### Endpoint

- `POST /predict`

#### Request Body

```json
{
    "population": 50000
}
```
Response Example

```json
{
    "message": "For a city with a population of 50,000, the estimated annual profit is $25,000.00.",
    "population": 50000,
    "predicted_profit": "$25,000.00"
}
```
Installation
To clone this repository to your local machine, you can use the following command:

```bash
git clone https://github.com/Shyanil/City-Expansion-Profit-Predictor
```
```
cd city-expansion-profit-predictor
```
```
python app.py
```
Usage
You can use a tool like Postman to send a POST request to http://127.0.0.1:5000/predict with the required JSON body.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

Acknowledgements

https://flask.palletsprojects.com/

https://numpy.org/doc/

https://pandas.pydata.org/docs/

https://matplotlib.org/stable/contents.html

https://seaborn.pydata.org/

