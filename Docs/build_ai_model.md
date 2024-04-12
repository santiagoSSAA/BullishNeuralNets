# Building the AI model with Tensorflow

In this section, we'll dive into the process of building and training a neural network model using TensorFlow, one of the most popular open-source libraries for machine learning. This model will be used to predict future stock prices based on the historical data we collected and preprocessed in the previous step.

## Introduction to neural networks and their application in time series prediction

[Neural networks](https://www.youtube.com/watch?v=rEDzUT3ymw4&ab_channel=SamuelArzt) are a type of machine learning model inspired by the structure and function of the human brain. They are particularly well-suited for tasks such as pattern recognition, image classification, and time series prediction, which is our focus in this project.

[Time series prediction](https://www.youtube.com/watch?v=wGUV_XqchbE&ab_channel=DataScienceDojo) involves using historical data to forecast future values. **Neural networks can learn from the patterns and trends present in the historical data, and then make predictions about future values based on that learned knowledge.**

## Preparing data for model training

Before we can train our neural network model, we need to prepare the data in a format suitable for training. This typically involves splitting the data into training and testing sets, scaling the features, and creating input sequences and target outputs.

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, shuffle=False)

# Create input sequences and target outputs
def create_sequences(data, seq_length=30):
    x, y = [], []
    for i in range(len(data) - seq_length):
        x.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(x), np.array(y)

# Scale the data
scaler = MinMaxScaler()
train_data_scaled = scaler.fit_transform(train_data)
x_train, y_train = create_sequences(train_data_scaled)
```
In this example, we split the data into training and testing sets, create input sequences and target outputs using a function `create_sequences`, and scale the data using the `MinMaxScaler` from scikit-learn.


## Building the neural network model with Tensorflow

With the data prepared, we can now build our neural network model using TensorFlow. Here's an example of how we can define and compile a simple recurrent neural network (RNN) model:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Define the model architecture
model = Sequential([
    LSTM(64, input_shape=(x_train.shape[1], x_train.shape[2])),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')
```

In this example, we define a sequential model with an LSTM (**Long Short-Term Memory**) layer and a Dense output layer. The LSTM layer is responsible for learning the patterns and dependencies in the input sequences, while the Dense layer outputs a single value, which is the predicted stock price.

## Model training & evaluation

With the model defined, we can now train it on the prepared training data:

```python
# Train the model
model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.1)
```
This code trains the model for **50 epochs**, with a batch **size of 32**, and **uses 10% of the training data** for validation during training.

After training, we can evaluate the model's performance on the test data:

```python
# Make predictions on the test data
x_test, y_test = create_sequences(test_data_scaled)
y_pred = model.predict(x_test)

# Inverse scale the predictions and calculate metrics
y_pred_rescaled = scaler.inverse_transform(y_pred)
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Calculate evaluation metrics (e.g., mean squared error, mean absolute error)
mse = mean_squared_error(y_test_rescaled, y_pred_rescaled)
mae = mean_absolute_error(y_test_rescaled, y_pred_rescaled)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
```
In this example, we make predictions on the test data, inverse scale the predictions and true values, and calculate evaluation metrics such as mean squared error (MSE) and mean absolute error (MAE) to assess the model's performance.

***By following these steps, you'll have a trained neural network model that can predict future stock prices based on historical data. In the next section, we'll learn how to integrate this model into a Flask web application, allowing users to interact with the model and visualize the predictions.***