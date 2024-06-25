import pandas as pd
from flask import Flask, render_template, request, jsonify

# from model import loal_model, preprocess_data

app = Flask(__name__)

messages = [
    {"text": "Hello and thank you for visiting MDBootstrap. Please click the video below.", "avatar": "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"},
    {"text": "Thank you, I really like your product.", "avatar": "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava2-bg.webp"}
]

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

@app.route('/get-messages', methods=['GET'])
def get_messages(): 
    return jsonify(messages)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    new_message = {
        "text": data.get('text'),
        "avatar": "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"  # Assuming a default avatar for new messages
    }
    messages.append(new_message)
    return jsonify({"message": "Message received successfully"})

@app.route('/chart-data', methods=['GET'])
def chart_data():
    data = {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        'values': [65, 59, 80, 81, 56, 55, 40]
    }
    return jsonify(data)

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