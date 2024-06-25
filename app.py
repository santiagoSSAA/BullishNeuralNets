import pandas as pd
from flask import Flask, render_template, request

# from model import loal_model, preprocess_data

app = Flask(__name__)

def predict_stock_price(stock_symbol):
    return "some_response¿?"

def create_mock_dataframe():
    # Define mock data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': ['foo', 'bar', 'baz', 'qux', 'quux'],
        'C': [0.1, 0.2, 0.3, 0.4, 0.5],
        'D': ['Yes', 'No', 'Yes', 'No', 'Yes']
    }
    df = pd.DataFrame(data)
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the stock symbol from the form
        stock_symbol = request.form['stock_symbol']
        
        print(stock_symbol)
        
        # Make a prediction using the trained model
        prediction = predict_stock_price(stock_symbol)
        
        # Render the result template with the prediction
        return render_template('result.html', prediction=prediction)
    
    table = create_mock_dataframe().to_html(
        classes="table table-striped table-sm", index=False, justify="left"
    )
    return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)