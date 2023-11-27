import streamlit as st
from datetime import date
from streamlit_timeline import timeline

def main():
    st.title('Projektplanung mit Gantt-Chart')

    # Datumsauswahl für die Projektzeitachse
    start_date = st.date_input('Startdatum des Projekts', date(2023, 1, 1))
    end_date = st.date_input('Enddatum des Projekts', date(2023, 12, 31))

    # Projekt-Details
    st.subheader('Projekt Details')
    project_name = st.text_input('Projektname')
    project_description = st.text_area('Projektbeschreibung')

    # Aufgabenliste
    st.subheader('Aufgabenliste')
    num_tasks = st.number_input('Anzahl der Aufgaben', min_value=1, value=1)

    tasks = []
    for i in range(num_tasks):
        task_name = st.text_input(f'Aufgabe {i + 1} - Name')
        task_start = st.date_input(f'Aufgabe {i + 1} - Startdatum', value=start_date)
        task_end = st.date_input(f'Aufgabe {i + 1} - Enddatum', value=end_date)
        tasks.append({
            'Task': task_name,
            'Start': task_start,
            'End': task_end
        })

    # Gantt-Chart erstellen und anzeigen
    st.subheader('Gantt-Chart')
    if st.button('Generiere Gantt-Chart'):
        df = timeline(tasks)
        st.write(df)

if __name__ == '__main__':
    main()
