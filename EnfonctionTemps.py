import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from lecture import seisme
from scipy.stats import chi2_contingency

token = 'pk.eyJ1IjoiY2xlbWVudGoiLCJhIjoiY2xoYWh4NTYwMDc3azNjbnM2em9veHdxbCJ9.xyrycPiUE7fNHDMvZN3zDw'

fdata1 = seisme
fdata1['instant'] = pd.to_datetime(fdata1['instant'])  # on met en datetime
fdata1 = fdata1.sort_values('instant')
fig = go.Figure()


# Tracer les tremblements de terre sur la carte à chaque instant
"""fig.add_trace(go.Scattermapbox(
    lat=fdata1['lat'],
    lon=fdata1['lon'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=fdata1['mag'] * 5,
        color=fdata1['profondeur'],
        colorscale='Viridis',
        showscale=True
    ),
    text=fdata1['pays'] + '<br>Magnitude: ' + fdata1['mag'].astype(str) + '<br>Profondeur: ' + fdata1['profondeur'].astype(str),
))"""

# Paramètres de la carte
fig.update_layout(
    mapbox=dict(
        accesstoken=token,
        center=dict(lat=fdata1['lat'].mean(), lon=fdata1['lon'].mean()),
        zoom=1
    ),
    showlegend=False
)

# Tracer l'évolution temporelle de l'activité sismique
fig.update_layout(
    title='Évolution temporelle de l\'activité sismique',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Magnitude')
)

# Afficher la figure
fig.show()

# Tester l'indépendance entre les colonnes 'mag' et 'profondeur'
cross_tab = pd.crosstab(fdata1['mag'], fdata1['profondeur'])
chi2, p, _, _ = chi2_contingency(cross_tab)
print(f"Statistique de test chi2: {chi2}")
print(f"Valeur p: {p}")
