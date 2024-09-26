"""Chatbot module specific for alpha vantage API prompts"""


import streamlit as st
from utils.openai_singleton import OpenAIClientSingleton
from utils.validations import validate_investment_intent
from utils.system_prompts import PROMPT_FOR_ANALYSIS


class Chatbot:
    """Chatbot class for instance in another projects"""

    def __init__(self, api_client, title="Stock Info Chatbot", model="gpt-3.5-turbo"):
        """
        Initialize the chatbot with a title, a default model, and Alpha Vantage API key.

        :param title: Title for the chatbot section
        :param model: OpenAI model to use (default: gpt-3.5-turbo)
        :param alpha_vantage_key: API key for Alpha Vantage
        """
        self.api_client = api_client
        self.title = title
        self.model = model
        self.client = self.initialize_openai_client()

    def initialize_openai_client(self):
        """Initialize the OpenAI client with the API key."""
        try:
            return OpenAIClientSingleton(api_key=st.secrets["OPENAI_API_KEY"]).get_client()
        except KeyError:
            st.error("API key not found in secrets.")
            return None

    def generate_response(self, prompt):
        """Generate a response based on the user's query."""
        validation_response: dict = validate_investment_intent(prompt)

        if not validation_response.get("intent"):
            return "I can only provide stock information. Please ask about a stock symbol."

        symbol = validation_response.get("stock_name")
        stock_data = self.api_client.query_time_series_daily_adjusted(symbol)
        if isinstance(stock_data, str):
            return stock_data

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": PROMPT_FOR_ANALYSIS.format(
                    prompt, stock_data, symbol)}
            ]
        )
        response = stream.choices[0].message.content
        return response

    def render(self):
        """Render the chatbot section in the Streamlit app."""
        st.subheader(self.title)  # Title for the chatbot section

        # Input prompt from user
        if prompt := st.chat_input("Ask me about stocks!"):
            with st.chat_message("user"):
                st.markdown(prompt)
            if self.client:
                with st.chat_message("assistant"):
                    response = self.generate_response(prompt)
                    st.markdown(response)
