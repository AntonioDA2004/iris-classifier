# Iris Classifier API

Flask API for Iris flower species prediction using machine learning.

## Features

- REST API endpoint for Iris flower classification
- Machine learning model trained on the classic Iris dataset
- Predicts between three Iris species: Setosa, Versicolor, and Virginica
- Accepts four flower measurements as input

## Requirements

- Python 3.12
- Flask
- scikit-learn
- pandas
- numpy

## Installation

1. Clone the repository
```bash
git clone https://github.com/AntonioDA2004/iris-classifier-api.git
cd iris-classifier-api
```

2. Create and activate virtual environment
```bash
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install scikit-learn pandas mlflow dvc flask
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
Invoke-RestMethod -Uri "http://localhost:5001/predict" -Method Post -ContentType "application/json" -Body '{"features":[5.1,3.5,1.4,0.2]}'
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
