from flask import Flask, request, jsonify
import pickle
import statsmodels.api as sm
import pandas as pd
import json


def preprocess_data(dataframe):
    '''
    Removed any first-party information regarding data processing. 

    Important thing here is to coerce the inference record into a form that the model expects.

    This implies that we would need to mimic all preprocessing/feature engineering from training.

    '''
    return dataframe



app = Flask(__name__) # Run a flask app that can be called by curl
with open('model.pkl', 'rb') as model_file:
    logit_model = pickle.load(model_file)

    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Perform necessary data preprocessing on 'data'
        if isinstance(data, dict): # Single JSON call
            df = pd.DataFrame([data])
        if isinstance(data, list): # List of JSON objects. 
            df = pd.DataFrame(data)
        df = preprocess_data(df)
        # Make predictions and add them to the df.
        df['phat'] = logit_model.predict(df)
        # Sort the columns alphabetically 
        df = df.reindex(sorted(df.columns), axis=1)
        # Return predictions as JSON
        return df.to_json(orient='records')
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8080)  # Ensure it runs on port 8080
