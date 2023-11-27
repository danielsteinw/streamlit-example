import streamlit as st

# Definiere die Funktionen für die Rechenoperationen
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division durch Null"

# Streamlit App
st.title('Einfacher Taschenrechner')

# Benutzer-Eingaben für Zahlen und Operation auswählen
num1 = st.number_input('Gib die erste Zahl ein')
num2 = st.number_input('Gib die zweite Zahl ein')

operation = st.selectbox(
    'Wähle die Operation',
    ('Addition', 'Subtraktion', 'Multiplikation', 'Division')
)

result = 0

# Je nach ausgewählter Operation den entsprechenden Rechenprozess aufrufen
if operation == 'Addition':
    result = add(num1, num2)
elif operation == 'Subtraktion':
    result = subtract(num1, num2)
elif operation == 'Multiplikation':
    result = multiply(num1, num2)
elif operation == 'Division':
    result = divide(num1, num2)

# Ergebnis ausgeben
st.write(f'Das Ergebnis der {operation} von {num1} und {num2} ist: {result}')
