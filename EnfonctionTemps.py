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
#fig = go.Figure()
#fig.show()

plt.hist(fdata1['instant'], len(fdata1['instant']), weights=fdata1['mag'])
plt.title('Évolution temporelle de l\'activité sismique')
plt.xlabel('date')
plt.show()

# chi2 entre 'mag' et 'instant'
cross_tab = pd.crosstab(fdata1['mag'], fdata1['instant'])
chi2, p, _, _ = chi2_contingency(cross_tab)
print(f"Statistique de test chi2: {chi2}")
print(f"Valeur p: {p}")
