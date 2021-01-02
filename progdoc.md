# LE MORPION par Marie Gabillault et Salimatou Traore

## ORGANIGRAMME

L'organisation de notre code est representé ici de manière schématique à l'aide de cet organigramme : 

![Organigramme](https://github.com/salimatoutraore/projet-python/blob/main/lorganigramme.png "Organigramme")


## Explications de chaques fonctions

Le jeu demarre grâce aux lignes de codes suivantes :

```python
if __name__ == '__main__':

    imax = int(input('Choisi une taille de grille : ')) 
    taille_reel_grille = imax**2 #taille 2D de la grille

    alig=int(input('Difficulté : Choisi un nombre de symbole à aligner dans la grille : ')) 

    nombre_partie_a_jouer=int(input('Combien de partie voulez vous jouer ? : '))

    symb='X' #symbole du premier joueur

    compteur_x=0 #Compteurs qui  permet de compter les victoires du joueurs X
    compteur_o=0 #Compteurs qui  permet de compter les victoires du joueurs O

    jeu(imax,taille_reel_grille,alig,nombre_partie_a_jouer)
```

1. Étape 1 : L'initialisation du jeu

L'initiation du jeu se fait à l'aide de l'utilisateur, en lui demandant la taille de la grille, le nombre de symbole à aligner ainsi que le nombre de partie à jouer : 

```python
imax = int(input('Choisi une taille de grille : ')) 
taille_reel_grille = imax**2 #taille 2D de la grille
alig=int(input('Difficulté : Choisi un nombre de symbole à aligner dans la grille : ')) 
nombre_partie_a_jouer=int(input('Combien de partie voulez vous jouer ? : '))
```

2. Étape 2 : Le début du jeu

Après l'initialisation, le jeu se lance grâce à la fonction ``` jeu ``` :

```python

def jeu(imax,taille_reel_grille,alig,nombre_partie_a_jouer):
    global symb
    for k in range(nombre_partie_a_jouer): #permet de jouer un certain nombre de partie
        print('Partie '+str(k+1)+ ' :')
        grille=contruction_grille(imax) #construction de la grille de taille imax
        while (verification(grille,alig,imax)): #tant qu'il y a des cases vides
            case_choisie=int(input('Le joueur '+symb+' choisi une position dans la grille entre 0 et '+str((taille_reel_grille)-1)+' : '))
            if(not(-1<case_choisie<taille_reel_grille)):
                continue

            y=case_choisie %imax
            x=int(case_choisie/imax)
            jouer(grille,x,y,imax,taille_reel_grille)

            if not(verification_victoire(x,y,imax,alig,grille)): #permet de stopper le jeu lorsque l'un des joueur gagne
                break

```
Nous avons tout d'abord une boucle for qui permet de jouer un nombre précis de parties.

Ensuite, nous faisons appelle aux autres fonctions du jeu : construction_grille (étape 3), verification (étape 4), jouer (étape 6) verification_victoire (étape 7),    

3. Étape 3 : La construction de la grille initiale

```python

def contruction_grille(imax): #Permet de créer la grille initiale du jeu en utilisant des tiretspour une lisibilité plus optimale
    grille=[] 
    print('-----'*imax)
    for i in range(0,imax):
        grille.append([])

        for j in range(0,imax):
    
            grille[i].append(' ')
        print(grille[i])
        print('-----'*imax)
    return grille

```


4. Étape 4 : 
5. Étape 5 : 
6. Étape 6 : 
7. Étape 7 : 
8. Étape 8 : 
