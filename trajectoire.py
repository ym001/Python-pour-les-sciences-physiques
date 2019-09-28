#Fichier contenant la fonction nécessaire au calcul de la trajectoire

#Importation des modules
import numpy as np
import matplotlib.pylab as plt

#Création de la fontion "traj"
def portee(m,g,k,h,Tx,v,angle):
    #Nombre de pas maximum
    Np=100000

    #Pas de temps en seconde
    Dt=1E-2
  
    #Initialisation des coordonnées du système
    t=np.zeros(Np+1)
    x=np.zeros(Np+1)
    y=np.zeros(Np+1)
    vx=np.zeros(Np+1)
    vy=np.zeros(Np+1)

    #Position initiale de la particule
    x[0]=0
    y[0]=h

    #Coordonnées du vecteur vitesse initiale au moment du lancer
    vx[0]=v*np.cos(angle/180*np.pi)
    vy[0]=v*np.sin(angle/180*np.pi)


    ######################################################
    #BOUCLE de mouvement de la particule
    ######################################################

    #La boucle
    p=0
    while y[p]>=0:

        #La valeur de l'instant en cours
        t[p+1]=t[p]+Dt

        #Les coordonnées de la somme des forces appliquées au système :
        Fx=0-k*vx[p]+Tx
        Fy=-m*g-k*vy[p]

        #Les coordonnées de la variation du vecteur vitesse :
        Dvx=Fx/m*Dt
        Dvy=Fy/m*Dt

        #Les coordonnées du vecteur vitesse à l'instant t+Dt :
        vx[p+1]=vx[p]+Dvx
        vy[p+1]=vy[p]+Dvy

        #Les coordonnées du système à l'instant t+Dt :
        x[p+1]=x[p]+vx[p]*Dt
        y[p+1]=y[p]+vy[p]*Dt

        p=p+1

    return max(x)
    

