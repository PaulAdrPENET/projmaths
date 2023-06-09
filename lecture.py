import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd
import plotly_express as px
from scipy.stats import chi2_contingency

# 1
seisme = pd.read_csv('seismes_2014.csv')
print(seisme)

# 2
nb_seisme = len(seisme)
print('Nombre seisme = ', nb_seisme)

# 3
noms = seisme.value_counts('pays', ascending=False).head(20)
print(noms)

# 4
#sns.load_dataset(noms)
#sns.boxplot(x="pays", y = "mag", data = )

# 4
seisme_data = seisme[seisme['pays'].isin(noms.index)]
print(seisme_data)
seaborn.boxplot(data=seisme_data, x="pays", y='mag', orient="v", dodge=False)

plt.xticks(rotation=90)
plt.show()

# Autre analyse sans les petits séismes
print("Autre analyse des seismes en écartant les séismes superflus")
seisme_big = seisme[seisme['mag'] >= 4]
seisme_data = seisme_big[seisme_big['pays'].isin(noms.index)]
print(seisme_data)
seaborn.boxplot(data=seisme_data, x="pays", y='mag', orient="v", dodge=False)
plt.xticks(rotation=90)
plt.show()

# 4b
seisme_max_mag_loc = seisme.groupby('pays')['mag'].idxmax()
seisme_max_mag_eq = seisme.loc[seisme_max_mag_loc]
seisme_mag_6 = seisme_max_mag_eq.sort_values('mag', ascending=False).head(6)
#seisme_mag_data = seisme[seisme['mag'].isin(seisme_mag.index)]
print("6 lieux du monde qui enregistre la plus forte magnitude: ")
print(seisme_mag_6[['pays', 'mag']])

# 4c
seisme_californie_alaska = list()
seisme_californie_alaska.append(seisme[(seisme['pays'] == 'Alaska') & (seisme["mag"] <= 2)])
seisme_californie_alaska.append(seisme[(seisme['pays'] == 'California') & (seisme["mag"] <= 2)])
print(seisme_californie_alaska)


# Etude supplémentaire de la relation entre profondeur et magnitude :
data = seisme[['mag', 'profondeur']]
fig = px.scatter(data, y='mag', x='profondeur')
fig.update_layout(title='Magnitude en fonction de la profondeur')
fig.show()

# Test d'indépendance Khi-deux entre profoneur et magnitude :
statistique, p_value,tmp1,tmp2, = chi2_contingency(pd.crosstab(data['profondeur'], data['mag']))
print("Statistique du test Khi-deux : ", statistique)
print("P_value du test : ", p_value)

