import numpy as np
import matplotlib.pylab as plt
### Le programme utilise une fonction d'un fichier annexe
import trajectoire

print("")
print("**************************")
print("* Portée d'un projectile *")
print("**************************")
print("")

### Données 
h=2.2		# Altitude initiale de la boule (m)
m=4.00	        # Masse du système (kg)
g=9.81	        # Norme du champ de pesanteur (N/kg)
Np=100000	# Nombre de pas maximal de calcul
Dt=1E-2	        # Pas de temps (s)

#######################################
### Données à modifier (question 4) ###
#######################################
v0=10		# Norme de la vitesse initiale (m/s)
k=0.1		# Coefficient de frottement k (N.s/m)
Tx=-10		# Force du vent Tx (N)

### Initialisation des tableaux
portee=np.zeros(91)
angle=np.zeros(91)

#############################################
### À compléter et modifier : question 3a ###
#############################################
### Indice qui sera modifié par la boucle for à introduire
n=0
### Angle de tir, à faire varier entre 0 et 90°
angle[n]=n
### Utilisation de la fonction "portee" 
### figurant dans le fichier annexe 
### pour déterminer les variations de x
portee[n]=trajectoire.portee(m,g,k,h,Tx,v0,angle[n])

### Identification de la portee maximale (ne pas modifier)
porteemax=int(100*portee[np.where(portee==np.max(portee))])/100
### Identification de l'angle optimal de lancer
angleopt=int(angle[np.where(portee==np.max(portee))])

### Affichage des données et de la portée
print("Données :")
print("- masse du système m =",m,"kg")
print("- hauteur de lancer h =",h,"m")
print("- norme de la vitesse initiale v0 =",v0,"m/s")
print("- coefficient de frottement k =",k,"N.s/m")
print("- force due au vent horizontal Tx =",Tx," N")
print("Portée du tir maximale :",porteemax,"m")
print("pour un angle de tir",angleopt,"°")
print("")

### Tracé de la portée en fonction de l'angle de tir
fig=plt.figure()
ax=fig.add_subplot(111,polar=True)
c=ax.plot(angle/180*np.pi,portee)
ax.set_thetamin(0)
ax.set_thetamax(90)
plt.title("Portée en fonction de l'angle de tir")
plt.show()
