import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
    st.title('Gantt-Chart Beispiel')

    # Dummy-Daten für Gantt-Diagramm
    data = {'Task': ['Aufgabe 1', 'Aufgabe 2', 'Aufgabe 3'],
            'Start': ['2023-01-01', '2023-02-01', '2023-03-01'],
            'End': ['2023-01-15', '2023-02-20', '2023-03-10']}
    df = pd.DataFrame(data)

    df['Start'] = pd.to_datetime(df['Start'])
    df['End'] = pd.to_datetime(df['End'])

    fig, ax = plt.subplots()
    for i, task in enumerate(df['Task']):
        ax.barh(task, df['End'][i] - df['Start'][i], left=df['Start'][i])

    st.pyplot(fig)

if __name__ == '__main__':
    main()
