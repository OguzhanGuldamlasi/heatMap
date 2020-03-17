import numpy as np
import pandas as pd
import seaborn as sns
import folium
import webbrowser
from folium.plugins import HeatMap # Call various libraries
posi=pd.read_excel("2020.xls") # Get seismic data stored on your computer
num = 59 #xx is the number of dataset
lat = np.array(posi["Enlem"][1:num]) # Get latitude value
lon = np.array(posi["Boylam"][1:num]) # Get the longitude value
# js = np.array(posi["js"][0:num],dtype=float) # Convert to numpy floating point data
data1 = [[lat[i],lon[i]] for i in range(57)] # Specification data format
map_osm = folium.Map(location=[39.925533,32.866287],zoom_start=7,control_scale=True)
#[x,x] is the center location, draw a Map, and start zooming is 5 times.
HeatMap(data1).add_to(map_osm) # Add heat map to the previously created map
file_path = "test.html"
map_osm.save(file_path) # Save as html file
webbrowser.open(file_path) # Default browser open