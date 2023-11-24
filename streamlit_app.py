import streamlit as st

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

    st.write('### Unfälle und Todesfälle nach Jahren')
    st.write('Year | Accidents | Fatalities\n---- | --------- | ----------\n2017 | 15000     | 1200\n2018 | 18000     | 1400\n2019 | 16000     | 1300\n2020 | 20000     | 1500\n2021 | 22000     | 1600')

    st.write('### Visualisierung der Unfallstatistik')

    st.write('#### Unfälle pro Jahr')
    st.text('2017: 15000, 2018: 18000, 2019: 16000, 2020: 20000, 2021: 22000')

    st.write('#### Todesfälle pro Jahr')
    st.text('2017: 1200, 2018: 1400, 2019: 1300, 2020: 1500, 2021: 1600')

if __name__ == "__main__":
    main()
