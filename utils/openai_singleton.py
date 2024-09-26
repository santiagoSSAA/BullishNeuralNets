"""This module contains the Singleton pattern for returning an OpenAI client"""
import openai


class OpenAIClientSingleton:
    """OpenAI Client Singleton Class"""
    _instance = None

    def __new__(cls, api_key):
        if cls._instance is None:
            cls._instance = super(OpenAIClientSingleton, cls).__new__(cls)
            openai.api_key = api_key
        return cls._instance

    def get_client(self) -> openai.OpenAI:
        """Get method for returning openai client"""
        return openai
