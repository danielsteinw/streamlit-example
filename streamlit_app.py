import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit as st

import streamlit as st

def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Kann nicht durch Null teilen"
    else:
        return a / b

def main():
    st.title('Einfacher Taschenrechner')

    operation = st.selectbox(
        'Wähle eine Operation',
        ('Addition', 'Subtraktion', 'Multiplikation', 'Division')
    )

    num1 = st.number_input('Gib die erste Zahl ein')
    num2 = st.number_input('Gib die zweite Zahl ein')

    result = 0

    if operation == 'Addition':
        result = addition(num1, num2)
    elif operation == 'Subtraktion':
        result = subtraktion(num1, num2)
    elif operation == 'Multiplikation':
        result = multiplikation(num1, num2)
    elif operation == 'Division':
        result = division(num1, num2)

    st.write(f'Das Ergebnis der {operation} ist: {result}')

if __name__ == "__main__":
    main()
