import folium
from folium.plugins import LocateControl

m = folium.Map()
LocateControl().add_to(m)
m.save('map/locatecontrol.html')
