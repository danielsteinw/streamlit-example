import streamlit as st
import wikipediaapi
import folium

def fetch_wiki_info(city):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(city)
    if page.exists():
        return page.summary
    else:
        return "Informationen nicht verfügbar."

def main():
    st.title('Stadtinformationen aus Wikipedia')

    # Koordinaten einiger Städte für die Karte
    cities = {
        'New York': (40.7128, -74.0060),
        'London': (51.5074, -0.1278),
        'Paris': (48.8566, 2.3522),
        'Tokyo': (35.6895, 139.6917)
    }

    selected_city = st.selectbox('Wähle eine Stadt:', list(cities.keys()))

    city_info = fetch_wiki_info(selected_city)

    st.write(f'### Informationen über {selected_city}')
    st.write(city_info)

    # Karte anzeigen
    map_center = cities[selected_city]
    folium_map = folium.Map(location=map_center, zoom_start=10)
    folium.Marker(location=map_center, popup=selected_city).add_to(folium_map)

    st.write('### Karte')
    folium_static(folium_map)

if __name__ == "__main__":
    main()
