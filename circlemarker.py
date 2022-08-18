
import folium
import pandas

data=pandas.read_csv("volcanos.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<=elevation<=2000:
        return 'red' 
    elif 2000<=elevation<=3000:
        return 'blue'
    else:
        return 'gray'           

map=folium.Map(location=[15.45245,76.34556],zoom_start=15,tiles='OpenStreetMap')
fgv=folium.FeatureGroup(name="volcanos")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln] ,radius=10,popup=str(el)+"m",fill_color=color_producer(el),color='grey',fill_opacity=0.7))

fgp=folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("webmapping.html")




'''

import folium
import pandas
 
data = pandas.read_csv("Volcanos.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="OpenStreetMap")
fg = folium.FeatureGroup(name = "My Map")
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
map.add_child(fg)
map.save("Map_html_popup_advanced.html")

'''