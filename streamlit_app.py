import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulierte Unfalldaten
def generate_fake_accident_data():
    data = {
        'Year': [2017, 2018, 2019, 2020, 2021],
        'Accidents': [15000, 18000, 16000, 20000, 22000],
        'Fatalities': [1200, 1400, 1300, 1500, 1600]
    }
    return pd.DataFrame(data)

def main():
    st.title('Fahrzeugsicherheit und Unfallstatistik')

    st.write('## Sicherheitsfunktionen')

    st.write('### Airbags')
    st.write('Airbags sind wichtige Sicherheitsvorrichtungen, die bei Unfällen die Insassen schützen.')

    st.write('### Antiblockiersystem (ABS)')
    st.write('ABS verhindert das Blockieren der Räder beim Bremsen und hilft dabei, die Kontrolle über das Fahrzeug zu behalten.')

    st.write('### Elektronische Stabilitätskontrolle (ESC)')
    st.write('ESC unterstützt bei der Stabilisierung des Fahrzeugs bei plötzlichen Richtungsänderungen oder Schleudern.')

    st.write('## Unfallstatistik')

    accident_data = generate_fake_accident_data()

    st.write('### Unfälle und Todesfälle nach Jahren')
    st.write(accident_data)

    st.write('### Visualisierung der Unfallstatistik')
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.barplot(x='Year', y='Accidents', data=accident_data, ax=axes[0])
    axes[0].set_title('Unfälle pro Jahr')

    sns.barplot(x='Year', y='Fatalities', data=accident_data, ax=axes[1])
    axes[1].set_title('Todesfälle pro Jahr')

    st.pyplot(fig)

if __name__ == "__main__":
    main()
