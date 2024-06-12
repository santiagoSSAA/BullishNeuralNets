import pandas as pd
from flask import Flask, render_template, request

# from model import loal_model, preprocess_data

app = Flask(__name__)

def predict_stock_price(stock_symbol):
    return "some_response¿?"

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
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)