# USAID Delivery Delay Predictor

## Overview
This project is a web-based application designed to predict delivery delays for products based on various input factors. It leverages machine learning to estimate delivery dates and provides users with an easy-to-use interface for predicting USAID shipment delivery delays.

## Motivation
Focusing on demonstrating the application of predictive modeling to decision making and pattern recognition in health care, I recognized one of the best solutions to a lack of health data was using supply chains. Using supply chains allowed the model to look for patterns and make decisions if I wanted to implement that feature in the future. 

## Learning Outcomes
The material for this project was almost entirely self-taught. I have never used Python or Flask for backend development and I had never worked with such large quantities of data prior to this project. Overall, the EDA and model tuning phases taught me the most about machine learning concepts and the front and back end connection taught me more about full-stack development.

## Challenges
This project was challenging for a number of reasons. Having almost no background prior in this type of predictive modeling prior to this project, the learning curve was exceptionally steep. I faced issues connecting the front and back ends, tuning the model, and selecting the best features for this model. 

## Features
- **User Interface**: 
  - Form-based input for transportation method, product category, vendor incoterm, country, and days since order.
  - Displays estimated delivery delay in days.

- **Backend**: 
  - Uses a `RandomForestRegressor` model to predict delivery delays.
  - Data preprocessing, feature engineering, and prediction are handled in Python scripts.

- **Frontend**: 
  - Simple HTML form to collect user inputs and display predictions.

## Technologies Used
- **Programming Languages**: Python, HTML
- **Libraries**: 
  - `pandas` for data manipulation
  - `joblib` for model and preprocessing object management
  - `scikit-learn` for machine learning and data preprocessing
  - `Flask` for the web server
- **Data Handling**: 
  - `KNNImputer` for missing value imputation
  - `LabelEncoder` for categorical feature encoding

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages listed in `requirements.txt`

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   
2. **Clone the Repository**
   ```bash
   pip install -r requirements.txt

3. Set up .env file
   ```bash
   BASE_DIR=path_to_your_directory
   MODEL_PATH=model.pkl
   LABEL_PATH=label_encoders.pkl
   IMPUTER_PATH=imputer.pkl
   COUNTRY_ENCODING_PATH=country_encoding.csv
   PRODUCT_LEADTIME_RATIO_PATH=product_leadtime_ratio.csv
   USAID_DATA=path_to_your_data.csv

4. Remove model.pkl from model.zip & run it
   ```bash
   python train_model.py

5. Start the flask application
   ```bash
   python run.py

