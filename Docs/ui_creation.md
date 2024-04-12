# 6. UI implementation

A well-designed user interface (UI) is crucial for creating an intuitive and engaging experience for users interacting with our stock price prediction web application. In this section, we'll focus on implementing an attractive and user-friendly UI using HTML, CSS, and JavaScript.

## User Interface Design with HTML, CSS & JavaScript

The UI design process typically starts with creating a mockup or wireframe to visualize the layout and structure of the web pages. Once the design is finalized, we can implement it using HTML for the content structure, CSS for styling and layout, and JavaScript for adding interactivity and dynamic behavior.

Here's an example of how we can structure the HTML for the main page of our application:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Stock Price Prediction</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Stock Price Prediction</h1>
      <form method="post">
        <label for="stock_symbol">Enter Stock Symbol:</label>
        <input type="text" id="stock_symbol" name="stock_symbol">
        <button type="submit">Predict</button>
      </form>
      <div id="prediction-result"></div>
    </main>
    <footer>
      <p>&copy; 2023 Stock Price Prediction</p>
    </footer>
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
  </body>
</html>
```
In this HTML structure, we have a header with a navigation menu, a main content area with a heading, a form for entering the stock symbol, a div for displaying the prediction result, and a footer. We also include links to external CSS and JavaScript files using Flask's `url_for` function to correctly reference static files.

For the CSS styling, we can create a `styles.css` file in a `static/css` directory and include rules for layout, typography, colors, and other visual aspects of the UI.

JavaScript can be used to add interactivity and handle events, such as form submissions or AJAX requests to fetch prediction results without refreshing the page. We can create a `app.js` file in a `static/js` directory and include JavaScript code to enhance the user experience.

## Creating a form to enter the symbol of the desired action

The form for entering the stock symbol is already present in the HTML structure shown above. Here's an example of how we can style the form using CSS:

```css
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  margin-bottom: 10px;
}

input[type="text"] {
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

button[type="submit"] {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```
This CSS code styles the form elements, including the label, input field, and submit button. It centers the form elements, adds spacing and borders, and styles the submit button with a green background color and white text.

## Viewing prediction results

To display the prediction results, we can use the `prediction-result` div in the HTML structure. Here's an example of how we can update this div using JavaScript:

```javascript
// app.js

// Add event listener to the form
const form = document.querySelector('form');
form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent form submission

  const stockSymbol = document.getElementById('stock_symbol').value;

  try {
    // Send AJAX request to Flask route to get prediction
    const response = await fetch(`/predict?stock_symbol=${stockSymbol}`, {
      method: 'GET',
    });

    if (response.ok) {
      const prediction = await response.json();
      const resultDiv = document.getElementById('prediction-result');
      resultDiv.innerHTML = `<p>Predicted Stock Price: ${prediction.price}</p>`;
    } else {
      console.error('Error fetching prediction');
    }
  } catch (error) {
    console.error('Error:', error);
  }
});
```
In this JavaScript code, we add an event listener to the form's `submit` event. When the form is submitted, we prevent the default form submission behavior and instead send an AJAX request to a Flask route (`/predict`) with the stock symbol as a query parameter.

If the response is successful, we parse the JSON response and update the `prediction-result` div with the predicted stock price. If there's an error, we log it to the console.

You'll need to create a Flask route (`/predict`) that accepts the stock symbol, makes a prediction using the trained model, and returns the prediction result as a JSON response.

***By following these steps, you'll have an attractive and user-friendly UI that allows users to enter a stock symbol, submit the form, and view the prediction result dynamically without refreshing the page.***