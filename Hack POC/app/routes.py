from flask import render_template, request
from app import app
from .predict import predict_delivery_delay  # Import the prediction function

@app.route('/', methods=['GET', 'POST'])
def index():
    delivery_delay = None
    error_message = None

    if request.method == 'POST':
        try:
            # Collect input data from the form
            transportation_method = request.form.get('transportation_method', '')
            product_category = request.form.get('product_category', '')
            vendor_incoterm = request.form.get('vendor_incoterm', '')
            country = request.form.get('country', '')
            days_since_order = int(request.form.get('days_since_order', 0))

            # Validate inputs
            if not transportation_method or not product_category or not vendor_incoterm or not country:
                raise ValueError("All input fields are required.")

            # Use the prediction function from predict.py
            delivery_delay = predict_delivery_delay(transportation_method, product_category, vendor_incoterm, country, days_since_order)

        except Exception as e:
            error_message = str(e)

    return render_template('index.html', delivery_delay=delivery_delay, error_message=error_message)
