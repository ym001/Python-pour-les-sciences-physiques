from math import *
import sys 

print("")
print("***************************************")
print("*          Bilan énergétique          *")
print("* système en glissement sur une pente *")
print("***************************************")
print("")

### Données ###
g=9.8	# norme du champ de pesanteur en newtons par kilogramme
yB=0	# altitude du point d'arrivée B en mètres
m=1	# masse du système en kilogrammes
L=20	# longueur de la piste en mètres
yA=10	# altitude du point de départ A en mètres
vA=0	# vitesse du système au départ en mètres par seconde
mu=0	# coefficient de frottement

### Tests d'interruption du programme ###
problemes=[]
if L<=0:
	problemes.append("L doit être strictement positive")
if m<=0:
	problemes.append("m doit être strictement positive")
if vA<0:
	problemes.append("vA ne peut pas être négative")
if g!=9.8:
	problemes.append("g doit rester à 9,8 N/kg")
if yB!=0:
	problemes.append("yB doit rester nulle")
if L<yA-yB:
	problemes.append("L et le dénivelé sont incompatibles")
if yA<yB:
	problemes.append("A est au-dessous de B")
if mu<0:
	problemes.append("mu est négatif")
if mu!=0 and vA!=0:
	problemes.append("vA n'est pas nulle mais il y a des frottements")
if len(problemes)!=0:
	for i in range(len(problemes)):
		print(problemes[i])
	sys.exit("Modifiez les paramètres et réessayez")

### Fonction d'affichage des énergies en un point ###
def affiche_energies(point,Ec,Epp,Em):
	print("Valeurs des énergies du système en",point,":")
	print("- Énergie cinétique :",round(Ec,1),"J")
	print("- Énergie potentielle de pesanteur :",round(Epp,1),"J")
	print("- Énergie mécanique :",round(Em,1),"J")
	print("")

### Affichage des données ###
print("Données")
print("- Masse du système :",m,"kg") 
print("- Longueur de la piste :",L,"m") 
print("- Altitude du point de départ :",yA,"m") 
print("- Altitude du point d'arrivée :",yB,"m") 
print("- Vitesse initiale du système :",vA,"m/s") 
print("- Coefficient de frottement :",mu) 
print("")

### Angle alpha de la piste au-dessus de l'horizontale ###
alpha=asin(float((yA-yB)/L))
alphadegre=alpha*180/pi
print("Angle entre la piste et l'horizontale :",round(alphadegre,1),"°")
print("")

##########################################
######## Question 2 - à compléter ########
### test du glissement et interruption ###
##########################################



### Calcul et affichage des énergies en A ###
EcA=0.5*m*vA**2
EppA=m*g*yA
EmA=EcA+EppA
affiche_energies("A",EcA,EppA,EmA)

######################################################
##### À compléter : question 1a puis question 2 ######
### Utilisation du théorème de l'énergie mécanique ###
######################################################
if mu==0:
	print("Hypothèse de conservation de l'énergie mécanique")
	### Calcul de EmB
	
else:
	print("Hypothèse de la loi de frottement de Coulomb")
	### Calcul et affichage de la norme des frottements
	
	print("- Norme de la force de frottements :",round(f,1),"N")
	### Calcul et affichage du travail des frottements
	
	print("- Travail de la force de frottements :",round(Wf,1),"J")
	### Calcul de EmB
	

### Calcul des énergies et de la vitesse en B




### Affichage des valeurs finales ###
print("")
affiche_energies("B",EcB,EppB,EmB)
print("Valeur de la vitesse en B :",round(vB,1),"m/s")
print("")
