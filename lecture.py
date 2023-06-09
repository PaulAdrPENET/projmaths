import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd
import plotly.express as px
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


#Construction d'un tableau de contingence :

tableau = pd.crosstab(data['profondeur'], data['mag'])

#On applique le test d'indépendance Khi-deux sur le tableau de contingence :

statistique, p_value, _, _ = chi2_contingency(tableau)
print("Statistique du test Khi-2 : ", statistique)
print("P-value : ", p_value)

# Calcul de l'odds ratio du tableau de contingence :

odds_ratio = tableau.apply(lambda row: row / row.sum(), axis=1)
print("Tableau des odds-ratio :")
print(odds_ratio)