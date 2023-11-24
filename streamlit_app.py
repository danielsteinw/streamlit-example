import streamlit as st
import folium

# Vordefinierte Informationen zu den Städten
city_info = {
    'New York': "New York City ist eine der größten Städte der Welt...",
    'London': "London ist die Hauptstadt des Vereinigten Königreichs...",
    'Paris': "Paris ist die Hauptstadt Frankreichs und eine bedeutende...",
    'Tokyo': "Tokio ist die Hauptstadt Japans..."
}

def main():
    st.title('Stadtinformationen')

    cities = list(city_info.keys())
    selected_city = st.selectbox('Wähle eine Stadt:', cities)

    selected_city_info = city_info[selected_city]

    st.write(f'### Informationen über {selected_city}')
    st.write(selected_city_info)

    # Koordinaten der Städte für die Karte
    city_coordinates = {
        'New York': (40.7128, -74.0060),
        'London': (51.5074, -0.1278),
        'Paris': (48.8566, 2.3522),
        'Tokyo': (35.6895, 139.6917)
    }

    map_center = city_coordinates[selected_city]

    # Karte anzeigen
    folium_map = folium.Map(location=map_center, zoom_start=10)
    folium.Marker(location=map_center, popup=selected_city).add_to(folium_map)

    st.write('### Karte')
    st.write(folium_map._repr_html_(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
