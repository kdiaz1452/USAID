import pandas as pd
import joblib
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the paths from environment variables
base_dir = os.getenv('BASE_DIR')
model_path = os.path.join(base_dir, os.getenv('MODEL_PATH'))
label_path = os.path.join(base_dir, os.getenv('LABEL_PATH'))
imputer_path = os.path.join(base_dir, os.getenv('IMPUTER_PATH'))
country_encoding_path = os.path.join(base_dir, os.getenv('COUNTRY_ENCODING_PATH'))
product_leadtime_ratio_path = os.path.join(base_dir, os.getenv('PRODUCT_LEADTIME_RATIO_PATH'))

# Load the model and necessary components
model = joblib.load(model_path)
label_encoders = joblib.load(label_path)
imputer = joblib.load(imputer_path)

# Load the country encoding CSV file
country_encodings = pd.read_csv(country_encoding_path, index_col='Country')['Country_Target_Encoded'].to_dict()

# Load the product lead time ratio CSV file
leadtime_ratios = pd.read_csv(product_leadtime_ratio_path, index_col='Product Category')['Product_LeadTime_Ratio'].to_dict()

def preprocess_data(df):
    # Encode categorical features
    for feature, le in label_encoders.items():
        if df[feature].dtype == 'object':
            df[feature] = le.transform(df[feature])
    # Impute missing values
    df = pd.DataFrame(imputer.transform(df), columns=df.columns)
    return df

def calculate_product_lead_time_ratio(product_category, vendor_incoterm):
    # Use product lead time ratios from the CSV file
    return leadtime_ratios.get(product_category, 1.0)  # Default to 1.0 if category is not found

def get_country_encoded(country):
    return country_encodings.get(country, -1)  # Default value if country is not found

def predict_delivery_delay(transportation_method, product_category, vendor_incoterm, country, days_since_order):
    # Derive additional features
    product_lead_time_ratio = calculate_product_lead_time_ratio(product_category, vendor_incoterm)
    country_encoded = get_country_encoded(country)

    # Prepare input data for prediction
    data = {
        'Fulfillment_Transportation': [1 if transportation_method == 'RDC' else 0],
        'Product_LeadTime_Ratio': [product_lead_time_ratio],
        'Days Since Order Entry': [days_since_order],
        'Country_Target_Encoded': [country_encoded]
    }
    df = pd.DataFrame(data)
    
    # Preprocess data and make prediction
    df = preprocess_data(df)
    prediction = model.predict(df)
    return prediction[0]  # Return the delivery delay in days
