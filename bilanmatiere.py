print("")
print("*********************************")
print("*       Étude quantitative      *")
print("* d'une transformation chimique *")
print("*********************************")
print("")

############################
### À modifier : données ###
############################
### Listes des réactifs et de leurs nombres stoechiométriques
nom_reac=["MnO4-","Fe2+","H+"]
coef_reac=[1,5,8] 
### Listes des produits et de leurs nombres stoechiométriques
nom_prod=["Mn2+","Fe3+","H2O"]
coef_prod=[1,5,4]
### Quantités de matière initiales des réactifs et produits, en moles
### Écrire "nc" (non connu) si l'espèce est le solvant ou est en excès
n_reac=[0.1,0,1,"nc"] 
n_prod=[0,0,"nc"] 
### Rappel des valeurs par défaut
#nom_reac=["MnO4-","Fe2+","H+"]
#coef_reac=[1,5,8] 
#nom_prod=["Mn2+","Fe3+","H2O"]
#coef_prod=[1,5,4]
#n_reac=[0.1,0.1,"nc"] 
#n_prod=[0,0,"nc"] 

### Affichage de l'équation de la réaction
print("Équation de la réaction :")
equation=""
for i in range(len(nom_reac)):
	equation=equation+str(coef_reac[i])+" "+nom_reac[i]
	if i<len(nom_reac)-1:
		equation=equation+" + "
	else:
		equation=equation+"  --->  "
for i in range(len(nom_prod)):
	equation=equation+str(coef_prod[i])+" "+nom_prod[i]
	if i<len(nom_prod)-1:
		equation=equation+" + "                 
print(equation)
print("")
       
### Création d'une grandeur vide pour xmax
xmax=None

### Fonction : état du système pour un avancement x
def etat_systeme(x):  
	print("Réactifs :")
	for i in range(len(nom_reac)):                                     
		if n_reac[i]=="nc":
			print("  ",nom_reac[i],"est en excès")
		else:
			n_reac[i]=round(n_reac[i]-x*coef_reac[i],3)    
			print("  ",nom_reac[i],":",n_reac[i]," mol")
	print("Produits :")
	for i in range(len(nom_prod)):                                     
		if n_prod[i]!="nc":
			n_prod[i]=round(n_prod[i]+x*coef_prod[i],3)
			print("  ",nom_prod[i],":",n_prod[i]," mol")

### Affichage de l'état initial 
print("Quantités de matière à l'état initial")
etat_systeme(0)
print("")

#################################################
############ À modifier : question 3 ############
### Fonction qui calcule l'avancement maximal ###
#################################################



#############################################
###### À modifier : question 1 puis 3 #######
### Valeur de l'avancement final en moles ###
#############################################

xf=0.01

### Affichage de l'état pour l'avancement xf
if xf==xmax:
	print("Quantités de matière pour l'avancement maximal xmax =",xmax,"mol")
else:
	print("Quantités de matière pour l'avancement xf =",xf,"mol")
etat_systeme(xf)

#######################################
####### À modifier : question 5 #######
### Test du mélange stœchiométrique ###
#######################################



print("")
