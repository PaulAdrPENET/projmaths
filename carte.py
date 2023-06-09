# Partie 2 - Cartes des séismes dans le monde
import math

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

# heatmap des séismes
"""
fig = px.density_mapbox(Fdata2, lat='lat', lon='lon', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.update_layout(mapbox_style="outdoors", mapbox_accesstoken=token)
fig.show()
"""

# Carte avec mag >=3 :
# On ajoute à F une colonne avec la taille des points correspondant avec la magnitude
Fdata3 = seisme[seisme['mag'] >= 5]
Fdata3.insert(2, 'm', F['mag'].astype('int32'))
Fdata3.insert(7, 'size', (((10 + 10*(Fdata3['mag']-5))**2)**1/2).astype('int32'))
print(F)
fig2 = px.density_mapbox(F, lat='lat', lon='lon', z='mag', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain",)
fig2.update_layout(mapbox_style="outdoors", mapbox_accesstoken=token)
fig2.add_trace(px.scatter_mapbox(Fdata3, lat='lat', lon='lon', color='m', size='size',
                                 color_discrete_sequence=palette).data[0])
fig2.show()


# carte des séisme façon Minard
Fdata4 = seisme[(3 <= seisme['mag'])]# or seisme['mag'] <= 8)]
Fdata4.insert(2, 'm', F['mag'].astype('int32'))
Fdata4.insert(7,'size',(((10 + 10*(Fdata3['mag']-5))**2)**1/2).astype('int32'))
print(F)
# a modifié avec scatter_geo pour mettre la palette
fig3 = px.scatter_geo(Fdata4, lat='lat', lon='lon', projection="natural earth")

# fig3 = px.density_mapbox(F, lat='lat', lon='lon', z='mag', radius=10,
#                        center=dict(lat=0, lon=180), zoom=0,
#                        mapbox_style="stamen-terrain",)
fig3.update_layout(showlegend=True, coloraxis_showscale=False, mapbox_accesstoken=token)

# On rajoute les nuages de points par magnitude
size = 1
for i in range(3, 9, 1):
    seismes_i = Fdata4[Fdata4["m"] == i]
    size = 3
    # Calcul de taille Magnitude >=5
    if i >= 5:
        size = 10+10*(i-5)
    fig3.add_scattergeo(lat=seismes_i['lat'], lon=seismes_i['lon'], marker={"color": palette[i], 'size': size, 'opacity': 0.5}, name=i)

fig3.show()

Fdata4 = seisme[['mag']]
Fdata4.mag = Fdata4.mag.fillna(0)
Fdata4['mag'] = Fdata4['mag'].astype(int)
#seisme_mag_data = seisme[seisme['mag'].isin([3, 4, 5, 6, 7, 8])]
#Fdata4['mag'] = Fdata4['mag'].astype(int)
E = Fdata4.value_counts('mag', ascending=False)
E = E.astype(int)

# seisme_mag_data = seisme[seisme['mag'].isin(E.index)]
seisme_mag_data = seisme[seisme['mag'].isin([3, 4, 5, 6, 7, 8])]
fig = px.pie(seisme_mag_data, names='mag')
fig.show()

# Nombre de séisme par pays:
Fdata5 = seisme[['pays', 'mag']]
fig = px.pie(Fdata5, names='pays')
#fig.show()

