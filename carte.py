# Partie 2 - Cartes des séismes dans le monde

import lecture
from lecture import seisme
import plotly.express as px
import matplotlib

# 1
F = seisme[seisme['mag'] >= 3]
print(F)

F.insert(2, 'm', F['mag'].astype('int32'))
print(F['m'])

Fdata2 = F[F['mag'] < 5]  # data des magnitudes infèrieurs à 5
# 2
palette = {
    3: "hotpink",
    4: "green",
    5: "chocolate",
    6: "blue",
    7: "red",
    8: "black"
}
token = 'pk.eyJ1IjoiY2xlbWVudGoiLCJhIjoiY2xoYWh4NTYwMDc3azNjbnM2em9veHdxbCJ9.xyrycPiUE7fNHDMvZN3zDw'

fig = px.density_mapbox(Fdata2, lat='lat', lon='lon', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.update_layout(mapbox_style="outdoors", mapbox_accesstoken=token)
# fig.show()

# Carte avec mag > 5 :

# On ajoute à F une colonne avec la taille des points correspondant avec la magnitude
Fdata3 = seisme[seisme['mag'] >= 5]
Fdata3.insert(2, 'm', F['mag'].astype('int32'))
Fdata3.insert(7,'size',(((10 + 10*(Fdata3['mag']-5))**2)**1/2).astype('int32'))
print(F)
fig2 = px.density_mapbox(F, lat='lat', lon='lon', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain",)
fig2.update_layout(mapbox_style="outdoors", mapbox_accesstoken=token)
fig2.add_trace(px.scatter_mapbox(Fdata3, lat='lat', lon='lon', color='m', size='size',
                                 color_discrete_sequence=palette).data[0])
#fig2.show()


# carte des séisme façon Minard
Fdata4 = seisme[3 <= seisme['mag'] <= 8]
Fdata4.insert(2, 'm', F['mag'].astype('int32'))
Fdata4.insert(7,'size',(((10 + 10*(Fdata3['mag']-5))**2)**1/2).astype('int32'))
print(F)
# a modifié avec scatter_geo pour mettre la palette
fig3 = px.scatter_geo()
fig3 = px.density_mapbox(F, lat='lat', lon='lon', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain",)
fig3.update_layout(mapbox_style="outdoors", mapbox_accesstoken=token)
fig3.add_trace(px.scatter_mapbox(Fdata3, lat='lat', lon='lon', color='m', size='size',
                                 color_discrete_sequence=palette).data[0])
fig3.show()

import plotly.express as px
Fdata4 = px.data.tips()
fig = px.pie(Fdata4, values='mag', names='pays')
fig.show()

