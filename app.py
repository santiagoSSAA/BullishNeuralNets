"""Streamlit dashboard with chatbot integration"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from chatbot_alphavantage import Chatbot  # Import the chatbot class
from utils.alphavantage import AlphaVantageAPI

# Example function to render a dashboard with a chart


def render_dashboard():
    """Dummy render dashboard"""
    st.title("Dashboard with Analytics")

    # Example dataframe
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 17, 35, 29]
    }
    df = pd.DataFrame(data)

    # Display a table
    st.subheader("Data Table")
    st.dataframe(df)

    # Create and display a bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Values'])
    st.pyplot(fig)

# Main Streamlit app


def main():
    """Main function"""
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ['Dashboard', 'Chatbot', 'Search'])
    alpha_vantage_client = AlphaVantageAPI()

    if options == 'Dashboard':
        render_dashboard()
    elif options == 'Chatbot':
        # Create and render the chatbot instance
        chatbot = Chatbot(
            title="Stocks predictor Chatbot",
            api_client=alpha_vantage_client
        )
        chatbot.render()
    elif options == 'Search':
        alpha_vantage_client.render_search()


if __name__ == "__main__":
    main()
