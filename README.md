# Iris Classifier

Iris flower species prediction using machine learning.

## Features

- Predicts the species of an Iris flower using a trained machine learning model
- Accepts four input measurements: sepal length, sepal width, petal length and petal width

## Requirements

- Python 3.12
- mlflow
- flask

## Installation

1. Clone the repository
```bash
git clone https://github.com/AntonioDA2004/iris-classifier.git
cd iris-classifier
```

2. Create and activate virtual environment
```bash
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install mlflow flask
```

## Usage

1. Start MLflow UI to view experiment tracking (in another terminal)
```bash
mlflow ui
```

2. Train the model
```bash
python train.py
```

3. Start the Flask server
```bash
python app.py
```

4. Make a prediction request
```powershell
curl -X POST http://localhost:5001/predict \
     -H "Content-Type: application/json" \
     -d '{"features":[5.1,3.5,1.4,0.2]}'
```

## Project Structure
```
iris-classifier-api/ 
├── app.py # Flask application 
├── train.py # Model training script 
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
