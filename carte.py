# Partie 2 - Cartes des séismes dans le monde

import lecture
from lecture import seisme

# 1
F = seisme[seisme['mag'] >= 3]
print(F)

F.insert(2, 'm', F['mag'].astype('int32'))
print(F['m'])

# 2
