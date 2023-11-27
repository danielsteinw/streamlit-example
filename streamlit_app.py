import streamlit as st
import plotly.figure_factory as ff

def main():
    st.title('Gantt-Chart Beispiel')

    # Dummy-Aufgabenliste
    df = [
        dict(Task='Aufgabe 1', Start='2023-01-01', Finish='2023-01-15'),
        dict(Task='Aufgabe 2', Start='2023-02-01', Finish='2023-02-20'),
        dict(Task='Aufgabe 3', Start='2023-03-01', Finish='2023-03-10')
    ]

    fig = ff.create_gantt(df)
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
