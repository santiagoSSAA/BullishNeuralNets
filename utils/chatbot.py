"""Encapsulated chatbot class for Streamlit projects using OpenAI API"""

import streamlit as st
from openai_singleton import OpenAIClientSingleton
from validations import validate_investment_intent


class Chatbot:
    """Chatbot class for instance in another projects"""

    def __init__(self, title="Chatbot", model="gpt-3.5-turbo", history: bool = True):
        """
        Initialize the chatbot with a title and a default model.

        :param title: Title for the chatbot section
        :param model: OpenAI model to use (default: gpt-3.5-turbo)
        """
        self.history = history
        self.title = title
        self.model = model
        self.client = self.initialize_openai_client()
        self.initialize_session_state()

    def initialize_openai_client(self):
        """Initialize the OpenAI client with the API key."""
        try:
            return OpenAIClientSingleton(api_key=st.secrets["OPENAI_API_KEY"]).get_client()
        except KeyError:
            st.error("API key not found in secrets.")
            return None

    def initialize_session_state(self):
        """Initialize session state for messages and model if not already set."""
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = self.model

        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_chat_messages(self):
        """Display previous chat messages stored in session state."""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def generate_response(self):
        """Generate a response from OpenAI API."""

        # Get user message
        user_message = st.session_state.messages[-1]["content"]

        # Investment intent validation
        validation_response: dict = validate_investment_intent(user_message)

        if not validation_response.get("intent"):
            return st.write("I cannot process your request as it has no intent of investment.")

        stream = self.client.chat.completions.create(  # type: ignore
            model=st.session_state["openai_model"],
            messages=[
                {"role": message["role"], "content": message["content"]}
                for message in st.session_state.messages
            ],
            stream=True,
        )
        return st.write_stream(stream)

    def render(self):
        """Render the chatbot section in the Streamlit app."""
        st.subheader(self.title)  # Title for the chatbot section

        # Display chat history
        if self.history:
            self.display_chat_messages()

        # Input prompt from user
        if prompt := st.chat_input("Ask me anything..."):
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            if self.client:
                with st.chat_message("assistant"):
                    response = self.generate_response()
                    st.markdown(response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response})
