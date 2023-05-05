import matplotlib
import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd

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

# 4b
seisme_mag = seisme.value_counts('mag', ascending=False).tail(6)
seisme_mag_data = seisme[seisme['mag'].isin(seisme_mag.index)]
print("6 lieux du monde qui enregistre la plus forte magnitude: ")
print(seisme_mag_data[['pays', 'mag']])

# 4c
seisme_californie_alaska = list()
seisme_californie_alaska.append(seisme[(seisme['pays'] == 'Alaska') & (seisme["mag"] <= 2)])
seisme_californie_alaska.append(seisme[(seisme['pays'] == 'California') & (seisme["mag"] <= 2)])
print(seisme_californie_alaska)



