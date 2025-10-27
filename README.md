# Diabetes Prediction Web Application
![SS1](https://github.com/adityashelke04/Deploying_Machine_Learning_Model/blob/adcf00a9c2faeef55264c8c4fd97b08a630778d1/screenshot/Screenshot%202025-10-27%20203211.png)
A web application built with Streamlit that predicts whether a person is diabetic or not based on input health parameters, using a pre-trained machine learning model.

## Project Overview

This project offers a user-friendly interface to input patient health data and get an instant diabetes diagnosis prediction. It uses a saved machine learning model (Random Forest or other) to predict diabetes outcomes based on features like glucose level, blood pressure, BMI, and others.

## Features

- Interactive web UI for inputting health parameters
- Real-time diabetes prediction using a pre-trained model
- Displays diagnostic result as "diabetic" or "non-diabetic"

## Technologies Used

- Python 3
- Streamlit: Web app framework
- NumPy
- Pickle: Model serialization and loading
- Pre-trained Machine Learning model (.sav file)

## How It Works

- Loads a pre-trained diabetes prediction model
- Accepts user inputs for various health attributes
- Processes inputs into the required format
- Predicts diabetes status
- Displays prediction result on the web app

## Installation

pip install streamlit numpy scikit-learn


## Running the Web App

streamlit run diabetes_prediction_web_app.py


## Script: predictive-system.py

This script demonstrates command-line usage of the saved diabetes prediction model.

- Loads the pre-trained model
- Accepts hardcoded test input data
- Converts input into the appropriate shape for prediction
- Prints "The person is diabetic" or "The person is non-diabetic" based on model prediction

## Usage Example of predictive-system.py

python predictive-system.py


## Future Enhancements

- Input validation and error handling
- Deploying the web app on cloud platforms
- Add graphical visualizations of predicted results
- Expand to multi-disease prediction

## License

This project is open source and intended for educational uses.

---

