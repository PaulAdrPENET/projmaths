import matplotlib
import seaborn
import pandas as pd

# 1
seisme = pd.read_csv('seismes_2014.csv')
print(seisme)

# 2
nb_seisme = len(seisme)
print('Nombre seisme = ', nb_seisme)

# 3
noms = pd.DataFrame()

for pays in seisme["pays"]:
    noms.set_index = pays
    noms['pays'] = seisme.count(pays)

print(noms.index)
