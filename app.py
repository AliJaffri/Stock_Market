import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Magnificent 7 Stock Prices with Technical Analysis")

# Load Data
df = pd.read_excel("magnificent7.xlsx", parse_dates=["Date"])
df.set_index("Date", inplace=True)

# Stock selection
stock_list = df.columns.tolist()
selected_stock = st.selectbox("Select a stock", stock_list)

# Date filter
start_date = st.date_input("Start date", df.index.min())
end_date = st.date_input("End date", df.index.max())

# Filter data
if start_date < end_date:
    data = df.loc[start_date:end_date, [selected_stock]].copy()

    st.subheader(f"{selected_stock} Price Chart")
    st.line_chart(data)

    # Moving Average
    st.subheader("📈 Moving Average")
    ma_window = st.slider("Select MA window", 5, 100, 20)
    data[f"{selected_stock}_MA"] = data[selected_stock].rolling(ma_window).mean()
    st.line_chart(data)

    # Bollinger Bands
    st.subheader("📉 Bollinger Bands")
    rolling = data[selected_stock].rolling(ma_window)
    ma = rolling.mean()
    std = rolling.std()
    upper = ma + 2 * std
    lower = ma - 2 * std

    fig, ax = plt.subplots()
    ax.plot(data.index, data[selected_stock], label="Price")
    ax.plot(data.index, ma, label="MA", linestyle='--')
    ax.plot(data.index, upper, label="Upper Band", linestyle='--', alpha=0.7)
    ax.plot(data.index, lower, label="Lower Band", linestyle='--', alpha=0.7)
    ax.fill_between(data.index, lower, upper, color='gray', alpha=0.1)
    ax.legend()
    ax.set_title("Bollinger Bands")
    st.pyplot(fig)

    # Daily Returns
    st.subheader("📊 Daily Returns")
    returns = data[selected_stock].pct_change().dropna()
    st.line_chart(returns)

    # Volatility
    st.subheader("📊 Volatility (Rolling Std)")
    volatility = returns.rolling(ma_window).std()
    st.line_chart(volatility)

    # CSV Download
    st.download_button(
        label="Download Data as CSV",
        data=data.to_csv().encode('utf-8'),
        file_name=f"{selected_stock}_analysis.csv",
        mime='text/csv'
    )
else:
    st.error("End date must be after start date.")
