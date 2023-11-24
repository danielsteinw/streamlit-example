import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit as st

import streamlit as st

# Initialisierung der Abschnitte als verfügbar
abschnitt_1 = True
abschnitt_2 = True
abschnitt_3 = True
abschnitt_4 = True

def reserviere_abschnitt(abschnitt):
    global abschnitt_1, abschnitt_2, abschnitt_3, abschnitt_4
    if abschnitt == 1:
        abschnitt_1 = False
    elif abschnitt == 2:
        abschnitt_2 = False
    elif abschnitt == 3:
        abschnitt_3 = False
    elif abschnitt == 4:
        abschnitt_4 = False

def main():
    st.title('Reservierung Teststrecke')

    st.write('Verfügbarkeit der Abschnitte:')
    st.write(f'Abschnitt 1: {"Verfügbar" if abschnitt_1 else "Nicht verfügbar"}')
    st.write(f'Abschnitt 2: {"Verfügbar" if abschnitt_2 else "Nicht verfügbar"}')
    st.write(f'Abschnitt 3: {"Verfügbar" if abschnitt_3 else "Nicht verfügbar"}')
    st.write(f'Abschnitt 4: {"Verfügbar" if abschnitt_4 else "Nicht verfügbar"}')

    selected_section = st.selectbox('Wähle einen Abschnitt:', [1, 2, 3, 4])

    if st.button('Abschnitt reservieren'):
        reserviere_abschnitt(selected_section)
        st.success(f'Abschnitt {selected_section} wurde erfolgreich reserviert!')

if __name__ == "__main__":
    main()
