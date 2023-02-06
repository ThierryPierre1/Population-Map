import pandas as pd
import numpy as np
import folium
import webbrowser
from geopy.geocoders import Nominatim

# Read the data
df = pd.read_csv('/Users/thierrypierre/Documents/GitHub/Population-Map/data/Population_Race.csv')
population_byRace = df.groupby(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']).sum()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Create a map
geolocator = Nominatim(user_agent="race")
location = geolocator.geocode("United States")
places = [population_byRace]
map = folium.Map(location=[40.730610, -73.935242], zoom_start=5)

for i in places:
    place = geolocator.geocode(i)
    print (place.latitude, place.longitude)


# Create a map
#map = folium.Map(location=[40.730610, -73.935242], zoom_start=5)
#map.show_in_browser()

# Add a layer
#folium.Choropleth(population_byRace, geo_data=population_byRace, data=population_byRace, columns=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico'], key_on='feature.properties.a', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2, legend_name='Population').add_to(map)

# Save the map
#map.save('map.html')
#webbrowser.open('map.html', new=2)



# Create a map
#class Map:
#    def __init__(self, df):
#        self.df = df
#        self.map = folium.Map(location=[40.730610, -73.935242], zoom_start=5)
#        self.map.show_in_browser()
    
#    def add_layer(self, df):
#        self.df = df
#        self.map = folium.Map(location=[40.730610, -73.935242], zoom_start=5)
#        self.map.show_in_browser()

#folium.Choropleth(a, geo_data=b, data=c, columns=['a', 'b'], key_on='feature.properties.a', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2, legend_name='Population').add_to(map)

#def save(self, output_file):
#        self.map.save(output_file)
#        webbrowser.open(output_file, new=2)




##map = folium.Map(location=[40.730610, -73.935242], zoom_start=5)
##map.show_in_browser()