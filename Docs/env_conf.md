# 2. Environment configuration

## Install Python and the necessary libraries (Flask, TensorFlow, Pandas, Numpy, etc.)

To get started with the project, you'll need to have Python and several libraries installed on your system. Follow these steps to set up the development environment:

1. **Install Python:** Make sure you have Python installed on your machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/

2. **Install Required Libraries:** This project relies on several Python libraries, including Flask for web development, TensorFlow for machine learning, Pandas for data manipulation, and Numpy for numerical operations. You can install these libraries using pip, Python's package installer. Open your terminal or command prompt and run the following command:

        pip install flask tensorflow pandas numpy

***This command will install the latest versions of Flask, TensorFlow, Pandas, and Numpy.***

## Set up a Python virtual environment (optional but recommended)

It's generally a good practice to use a virtual environment for Python projects. A virtual environment is an isolated Python environment that allows you to install packages and dependencies specific to your project without affecting your system's global Python installation. To create a new virtual environment, navigate to your project directory and run the following command:

    python -m venv env

This command will create a new virtual environment named env in your project directory. To activate the virtual environment, run the following command:

- On Windows:

        env\Scripts\activate

- On macOS or Linux:

        source env/bin/activate

Once the virtual environment is activated, you should see (env) prefixed to your terminal prompt, indicating that the virtual environment is active. With the virtual environment active, you can install the required libraries by running the same pip install command as before:

        pip install flask tensorflow pandas numpy

This will install the libraries within the virtual environment, keeping your system's global Python installation untouched.

***After completing these steps, you'll have Python and all the necessary libraries installed and ready to use for the project. In the next section, we'll dive into obtaining historical stock data.***