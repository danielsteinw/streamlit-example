import streamlit as st
import pandas as pd
import random

def generate_fake_data():
    # Erzeugung von simulierten Aktiendaten für ein fiktives Unternehmen
    data = {
        'Date': pd.date_range(start='2022-01-01', end='2022-12-31'),
        'Close': [random.uniform(100, 200) for _ in range(365)]
    }
    return pd.DataFrame(data)

def main():
    st.title('Fiktive Aktienkursanalyse')

    stock_data = generate_fake_data()

    st.write('### Fiktive Aktiendaten')
    st.write(stock_data)

    st.write('### Statistik')
    st.write(stock_data['Close'].describe())

    st.write('### Diagramm')
    st.line_chart(stock_data.set_index('Date')['Close'])

if __name__ == "__main__":
    main()
