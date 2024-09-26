"""This module contains AI validations for chatbot"""

import json
import streamlit as st
from .openai_singleton import OpenAIClientSingleton
from .system_prompts import PROMPT_FOR_INVESTMENT_INTENT

client = OpenAIClientSingleton(
    api_key=st.secrets["OPENAI_API_KEY"]).get_client()


class JSONParseError(Exception):
    """Excepción personalizada para errores de análisis de JSON."""

    def __init__(self, message="Error al cargar el JSON"):
        self.message = message
        super().__init__(self.message)


def validate_investment_intent(prompt: str) -> dict:
    """Function to validate if a prompt has an investment intent"""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": PROMPT_FOR_INVESTMENT_INTENT},
            {"role": "assistant", "content": "Ok, I'm ready"},
            {"role": "user", "content": "¿Es un buen momento para comprar acciones de ETH?"},
            {"role": "assistant", "content": '{"intent": true, "stock_name": ETH}'},
            {"role": "user", "content": "¿Qué opinas sobre la música pop?"},
            {"role": "assistant", "content": '{"intent": false}'},
            {"role": "user", "content": "¿Qué opinas sobre las acciones de T10G.LON para los próximos seis meses?"},
            {"role": "assistant", "content": '{"intent": true, "stock_name": "T10G.LON"}'},
            {"role": "user", "content": "¿Las acciones de BTC están sobrevaloradas o infravaloradas?"},
            {"role": "assistant", "content": '{"intent": true, "stock_name": "BTC"}'},
            {"role": "user", "content": " ¿Qué hay de nuevo en el cine?"},
            {"role": "assistant", "content": '{"intent": false}'},
            {"role": "user", "content": "¿Es mejor comprar acciones de TSLA ahora o esperar?"},
            {"role": "assistant", "content": '{"intent": true, "stock_name": "TSLA"}'},
            {"role": "user", "content": " ¿Cuál es el riesgo de invertir en acciones del sector farmaceutico?"},
            {"role": "assistant", "content": '{"intent": false}'},
            {"role": "user", "content": "¿Qué dividendos paga microsoft y son atractivos?"},
            {"role": "assistant", "content": '{"intent": false}'},
            {"role": "user", "content": prompt}
        ]
    )
    reply_content: str = completion.choices[0].message.content
    try:
        response = json.loads(reply_content)
        return response
    except json.JSONDecodeError as e:
        raise JSONParseError(
            "AI validation retrieved an incorrect JSON format") from e
