# 5. Creating the Web Application with Flask

Now that we have a trained AI model for predicting stock prices, it's time to create a web application using Flask, a lightweight and popular Python web framework. This web application will serve as an interface for users to interact with our model and visualize the predictions.

## Basic structure of flask application


A Flask application consists of several components:

1. **Import statements:** We need to import the necessary modules and libraries, including Flask itself.

2. **Application instance:** We create an instance of the Flask class, which represents our web application.

3. **Routes and views:** We define routes and their corresponding view functions, which handle incoming requests and generate responses.

4. **HTML templates:** We create HTML templates to structure the content that will be rendered and displayed to the user.

5. **Running the application:** Finally, we include code to run the Flask application on a local development server.

Here's a basic example of a Flask application structure:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we import the `Flask` class and the `render_template` function from the `Flask` library. We create an instance of the Flask class and assign it to the variable `app`. We then define a route for the root URL (`/`) using the `@app.route` decorator, and associate the `index` function to handle requests to this route.

Inside the `index` function, we use the `render_template` function to render the `index.html` template. Finally, we include a conditional statement to run the Flask application in debug mode when the script is executed directly.

## Creating routes & views

For our stock prediction application, we'll need to create additional routes and views to handle user input and display the prediction results. Here's an example of how we can define a route to handle a form submission:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the stock symbol from the form
        stock_symbol = request.form['stock_symbol']
        
        # Make a prediction using the trained model
        prediction = predict_stock_price(stock_symbol)
        
        # Render the result template with the prediction
        return render_template('result.html', prediction=prediction)
    
    return render_template('index.html')

```
In this example, we define a route for the root URL (`/`) that can handle both GET and POST requests using the `methods` argument. Inside the `index` function, we check if the request method is POST, which means the user has submitted the form. We then retrieve the stock symbol from the form data using `request.form['stock_symbol']`.

Next, we call a function `predict_stock_price` (which we'll define later) to make a prediction using our trained model. Finally, we render the `result.html` template and pass the prediction as a variable.

## HTML Template rendering

Flask allows us to create HTML templates using the Jinja2 templating engine. Templates are stored in a directory called `templates` (you'll need to create this directory if it doesn't exist). Here's an example of what the `index.html` template might look like:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Stock Price Prediction</title>
  </head>
  <body>
    <h1>Stock Price Prediction</h1>
    <form method="post">
      <label for="stock_symbol">Enter Stock Symbol:</label>
      <input type="text" id="stock_symbol" name="stock_symbol">
      <button type="submit">Predict</button>
    </form>
  </body>
</html>
```
This template contains a form with an input field for the user to enter a stock symbol and a submit button. When the user submits the form, Flask will handle the POST request and render the `result.html` template with the prediction.

## Integration of the trained AI model into the application

To integrate our trained AI model into the Flask application, we need to create a function that takes a stock symbol as input, preprocesses the data, and uses the trained model to make a prediction. Here's an example of how we can implement this:

```python
import pandas as pd
from model import load_model, preprocess_data

# Load the trained model
model = load_model('model.h5')

def predict_stock_price(stock_symbol):
    # Fetch historical data for the stock symbol
    data = fetch_stock_data(stock_symbol)
    
    # Preprocess the data
    X = preprocess_data(data)
    
    # Make a prediction using the trained model
    prediction = model.predict(X)
    
    # Post-process the prediction (e.g., inverse scaling)
    prediction = postprocess_prediction(prediction)
    
    return prediction
```
In this example, we import functions from a hypothetical `model` module that loads the trained model (`load_model`) and preprocesses the data (`preprocess_data`). We define a function `predict_stock_price` that takes a stock symbol as input, fetches the historical data for that symbol (using a function `fetch_stock_data` that we'll define later), preprocesses the data using the `preprocess_data` function, makes a prediction using the trained model, and post-processes the prediction (e.g., inverse scaling) using a function `postprocess_prediction` (which we'll also define later).

***By following these steps, you'll have a Flask web application that allows users to input a stock symbol, makes a prediction using the trained AI model, and displays the prediction result to the user through a rendered HTML template.***

---

**In the next section, we'll cover how to implement a user-friendly interface for the web application.**