import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import webbrowser
from content import privacy_policy, bio, page_title, page_icon, url
from PIL import Image

Green="🟢 Positive Price Change From Yesterday's CLose"
Red="🔴 Negative Price Change From Yesterday's Close"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.sidebar.image("N_Technologies_Design.png")
st.markdown("""

    **Input different tickers in the navigation bar  to view stock and chart data**
            """)
st.sidebar.write(bio)
st.sidebar.tabs(["Welcome"])
st.markdown("""
    <style>
        body {
            background-color: #000;
        }
        .sidebar .sidebar-content {
            background-color: ##00FFFF;
        }
        .sidebar .sidebar-content .tabs {
            background-color: #000;
        }
        .sidebar .sidebar-content .tabs .tab {
            color: #0ff;
        }
        .sidebar .sidebar-content .tabs .tab.active {
            background-color: #0ff;
            color: #000;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([.5,1,2])
with col1:
    if st.sidebar.button('Chat With Us 👋'):
        webbrowser.open_new_tab(url)

with col2:
    privacy_policy_button = st.sidebar.button('Privacy Policy')
    if privacy_policy_button:
        st.write(privacy_policy)

slider_value = st.sidebar.slider("We Are Under Active Developement", 0, 100, 50)

with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:
        ticker_symbol = st.sidebar.text_input("Enter a ticker symbol:", value="TSLA")
        stock_data = yf.Ticker(ticker_symbol)
        data = stock_data.history(period="1mo", interval="30m")

        fig, ax = plt.subplots()
        ax.plot(data.index, data["Close"])
        ax.set_title(f'{ticker_symbol.upper()} Stock Price')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.grid(True)

        st.pyplot(fig)

    with col2:
        st.header("Stock Information")
        st.write(f"Company: {stock_data.info['longName']}")
        st.write(f"Current Price: ${stock_data.info['currentPrice']}")
        st.write(f"Previous Close: ${stock_data.info['regularMarketPreviousClose']}")
        st.write(f"Stock Float: {stock_data.info['floatShares']}")
        st.write(f"Market Cap: {stock_data.info['marketCap']}")
        #st.write(f"Dividends: {stock_data.info['dividendRate']}")
        st.write(f"Short Ratio: {stock_data.info['shortRatio']}")
        st.write(f"52 Week High: ${stock_data.info['fiftyTwoWeekHigh']}")
        st.write(f"52 Week Low: ${stock_data.info['fiftyTwoWeekLow']}")
        #st.write(f"Beta: {stock_data.info['beta']}")
        st.write(f"EPS: {stock_data.info['trailingEps']}")
        st.write(f"PE Ratio: {stock_data.info['trailingPE']}")
        st.write(f"recommendationKey: {stock_data.info['recommendationKey']}")
        st.write(f"Average Volume: {stock_data.info['averageVolume10days']}")
        st.write(f"volume: {stock_data.info['volume']}")

        if stock_data.info['regularMarketPreviousClose'] < stock_data.info['currentPrice']:
            st.write(f" {Green}")
        else:
            st.write(f" {Red}")    
