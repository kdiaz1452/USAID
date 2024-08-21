import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
import joblib
import os
from dotenv import load_dotenv

# Load environment variables from .env 
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

csv_file_path = os.getenv('USAID_DATA')

def preprocess_data(df):
    # Convert categorical features to numeric using LabelEncoder
    categorical_features = ['Fulfillment_Transportation', 'Country_Target_Encoded']
    label_encoders = {}

    for feature in categorical_features:
        if df[feature].dtype == 'object':
            le = LabelEncoder()
            df[feature] = le.fit_transform(df[feature])
            label_encoders[feature] = le

    return df, label_encoders

def train_and_save_model():
    df = pd.read_csv(csv_file_path, low_memory=False)

    features = ['Fulfillment_Transportation', 'Product_LeadTime_Ratio', 'Days Since Order Entry', 'Country_Target_Encoded']
    target = 'Delivery Delay'

    # Preprocess data
    df, label_encoders = preprocess_data(df)
    imputer = KNNImputer(n_neighbors=5)
    df[features] = imputer.fit_transform(df[features])
    df = df.dropna(subset=[target])

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model and preprocessing objects
    joblib.dump(model, 'model.pkl')
    joblib.dump(label_encoders, 'label_encoders.pkl')
    joblib.dump(imputer, 'imputer.pkl')

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    feature_importances = model.feature_importances_
    print("Feature Importances:")
    for feature, importance in zip(features, feature_importances):
        print(f"{feature}: {importance}")

if __name__ == '__main__':
    train_and_save_model()