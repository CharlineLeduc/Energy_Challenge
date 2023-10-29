#tau = transmissivitÃ© 
#K= AU = constante 
#Q_load = valeur totale de chauffage 
#T_out = tempÃ©rature extÃ©rieure 
#j = jour considÃ©rÃ©
# Formule : Q_load = K*delta_tau*Somme,j(15-T_out,j)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

T_out = pd.read_excel("T_out.xlsx", usecols="C")

#Donées B3 dans suivi conso fuel
#J'ai des données de conso à partir du 19/11/19 au 10/12/21 = 752 jours 
#au total on a 1487 + 1500 + 1007 + 1459 + 1866 + 1000 + 1000 = 9319 Unité ? 

Q_tot = (9319/ 752)*365 #Permet d'avoir une idée de la conso globale pour un an 
T_in = 18 #Degré (c'est une approximation)
#La boucle permet d'estimer AU sur un an , il faut que ce soit une constante dans il faudra faire la moyenne
#Peux-tu vérifier que c'est juste ? 
# Je ne suis pas certaine pour le Qtot, je pense qu'il faudrait un vecteur Q de la taille du vecteur T_out et AU dont la somme vaudrair Qtot? 
DeltaT=0
meanT = np.zeros(365)

for i in range(8760):
    DeltaT += T_in - T_out.Temperature[i]
    
AU = Q_tot / DeltaT
print(AU)
j=0

for i in range(0,8760,23):
    if j == 365 : 
        break
    else:
        meanT[j] = np.mean(T_out.Temperature[i:i+23])
        j += 1

Q_jour = np.zeros(365)
DeltaTJour = np.zeros(365)

for i in range(365):
    DeltaTJour[i] = T_in - meanT[i]
    
for i in range(365):
    if DeltaTJour[i] <= 0:
        Q_jour[i] = 0
    else:
        Q_jour[i] = AU*DeltaTJour[i]



font2 = {'family':'serif','color':'black','size':15}
plt.figure(figsize=(10, 6))
plt.plot(meanT,Q_jour)
plt.title("Energy signature over 2021", fontdict = font2)
plt.xlabel(r"Temperature (°C)",fontdict = font2)
plt.ylabel("Specific heat power [W/m^2]",fontdict = font2)
plt.grid()
plt.savefig('EnergySign.eps')
plt.show()

        

