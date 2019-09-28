import numpy as np
import matplotlib.pylab as plt

print("")
print("*****************************")
print("* Mouvement d'un projectile *")
print("*****************************")
print("")

### Données 
h=2.2		# Altitude initiale de la boule (m)
v0=10		# Norme de la vitesse initiale (m/s)
m=4.00	        # Masse du système (kg)
g=9.81	        # Norme du champ de pesanteur (N/kg)
Np=100000	# Nombre de pas maximal de calcul
Dt=1E-2	        # Pas de temps (s)

#######################################
### Données à modifier (question 2) ###
#######################################
angle=40	# Angle de lancer au-dessus de l'horizontale (°)
k=0		# Coefficient de frottement k (N.s/m)
Tx=0		# Force du vent Tx (N)

### Initialisation 
### Création de tableaux remplis de zéros
t=np.zeros(Np+1)
x=np.zeros(Np+1)
y=np.zeros(Np+1)
vx=np.zeros(Np+1)
vy=np.zeros(Np+1)
### Position initiale de la boule
x[0]=0
y[0]=h
### Coordonnées du vecteur vitesse initiale
vx[0]=v0*np.cos(angle/180*np.pi)
vy[0]=v0*np.sin(angle/180*np.pi)
### Pas de calcul
p=0

### Boucle de calcul du mouvement 
while y[p]>=0:
	# Calcul de la date 
	t[p+1]=t[p]+Dt
	########################################
	### À compléter : question 1a puis 2 ###
	########################################
	### Coordonnées de la somme des forces 
	Fx=
	Fy=
	### Coordonnées de la variation du vecteur vitesse
	Dvx=
	Dvy=
	### Coordonnées du vecteur vitesse à l'instant t+Dt
	vx[p+1]=
	vy[p+1]=

	### Ne pas modifier :
	### Coordonnées de la position à l'instant t+Dt
	x[p+1]=x[p]+vx[p]*Dt
	y[p+1]=y[p]+vy[p]*Dt
	### Avancement du pas de calcul
	p=p+1

##################################
#### À modifier : question 1b ####
### Détermination de la portée ###
##################################
portee=0	# Expression à modifier

### Affichage des données et de la portée
print("Données :")
print("- masse du système m =",m,"kg")
print("- hauteur de lancer h =",h,"m")
print("- norme de la vitesse initiale v0 =",v0,"m/s")
print("- angle de tir",angle,"°")
print("- coefficient de frottement k =",k,"N.s/m")
print("- force due au vent horizontal Tx =",Tx," N")
print("Portée du tir :",round(portee,2),"m") 
print("")

### Tracé de la trajectoire du système
plt.plot(x[0:p],y[0:p],'-',lw=2)
plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title("Trajectoire du système")
plt.grid(True)
plt.tight_layout()
plt.show()
