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

Après l'initialisation, le jeu se lance grâce à la fonction ``` jeu ```
