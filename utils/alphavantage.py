"""This module contains Alpha Vantage API support for getting Stock Market Info"""
import streamlit as st
import requests


class AlphaVantageAPI:
    """Alpha Vantage API Class"""

    def __init__(self):
        self.api_key = st.secrets["ALPHA_VANTAGE_API_KEYS"]
        self.base_url = "https://www.alphavantage.co/query"

    def _search_symbols(self, query, function="SYMBOL_SEARCH"):
        """Alpha vantage Search Symbol endpoint GET method"""
        params = {
            "function": function,
            "keywords": query,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params, timeout=20)
        if response.status_code != 200:
            st.error(f"Error: {response.status_code}")
            return None
        return response.json()

    def query_time_series_daily_adjusted(self, symbol: str):
        """Query the Alpha Vantage API for stock information."""
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(url, params=params, timeout=20)
        if response.status_code == 200:
            data = response.json()
            if "Time Series (Daily)" not in data:
                return "No data available for this symbol."
            return data
        return "Failed to fetch data."

    def render_search(self):
        """Render search symbol with Streamlit"""
        query = st.text_input("Enter a symbol or keyword to search:")
        if not query:
            return
        data = self._search_symbols(query)
        if not data:
            return
        matches = data.get('bestMatches', [])
        if not matches:
            st.write("No results found.")
            return
        st.write("### Search Results")
        for match in matches:
            st.write(f"**Symbol:** {match.get('1. symbol')}")
            st.write(f"**Name:** {match.get('2. name')}")
            st.write(f"**Type:** {match.get('3. type')}")
            st.write(f"**Region:** {match.get('4. region')}")
            st.write(f"**Market Open:** {match.get('5. marketOpen')}")
            st.write(
                f"**Market Close:** {match.get('6. marketClose')}")
            st.write(f"**Timezone:** {match.get('7. timezone')}")
            st.write("---")
