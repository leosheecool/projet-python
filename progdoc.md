# LE MORPION par Marie Gabillault et Salimatou Traore

## ORGANIGRAMME

L'organisation de notre code est representé ici de manière schématique à l'aide de cet organigramme : 

![Organigramme](https://github.com/salimatoutraore/projet-python/blob/main/lorganigramme.png "Organigramme")


## Explications de chacune des fonctions

Le jeu demarre grâce aux lignes de codes suivantes :

```python
if __name__ == '__main__':
    
    input('Bienvenue dans LE MEILLEUR jeu du Morpion ! Es-tu prêt ? (Oui ou Oui ?) : ')
    
    imax = int(input('Choisi une taille de grille : ')) 
    taille_reel_grille = imax**2 #taille 2D de la grille
    L=[j for j in range(1,taille_reel_grille+1)] 
    alig=int(input('Difficulté : Choisi un nombre de symbole à aligner dans la grille : ')) 

    nombre_partie_a_jouer=int(input('Combien de partie voulez vous jouer ? : '))

    symb='X' #symbole du premier joueur

    compteur_x=0 #Compteurs qui  permet de compter les victoires du joueurs X
    compteur_o=0 #Compteurs qui  permet de compter les victoires du joueurs O

    jeu(imax,taille_reel_grille,alig,nombre_partie_a_jouer,L)
```


***
***


1. Étape 1 : L'initialisation du jeu

L'initiation du jeu se fait d'une part à l'aide de l'utilisateur, en lui demandant la taille de la grille, le nombre de symbole à aligner ainsi que le nombre de partie à jouer. Et d'autre part, par l'initialisation d'une liste L qui contiendra les nombres de 1 à n (taille de la grille) qui permettront aux joueurs de se reperer dans la grille, des compteurs de victoirs et du premier symbole à être joué  : 

```python
imax = int(input('Choisi une taille de grille : ')) 
taille_reel_grille = imax**2 #taille 2D de la grille
L=[j for j in range(1,taille_reel_grille+1)] 
alig=int(input('Difficulté : Choisi un nombre de symbole à aligner dans la grille : ')) 

nombre_partie_a_jouer=int(input('Combien de partie voulez vous jouer ? : '))

symb='X' #symbole du premier joueur

compteur_x=0 #Compteurs qui  permet de compter les victoires du joueurs X
compteur_o=0 #Compteurs qui  permet de compter les victoires du joueurs O
```


***
***


2. Étape 2 : Le début du jeu

Après l'initialisation, le jeu se lance grâce à la fonction ``` jeu ``` :

```python

def jeu(imax,taille_reel_grille,alig,nombre_partie_a_jouer,L):
    global symb
    for k in range(nombre_partie_a_jouer): #permet de jouer un certain nombre de partie
        print('Partie '+str(k+1)+ ' :')
        grille=contruction_grille(imax,L) #construction de la grille de taille imax
        while (verification(grille,alig,imax,L)): #tant qu'il y a des cases vides
                
            while True: #Cette condition permet d'afficher à l'écran que la case choisi n'est pas valide (ce n'est pas un int) et qu'il faut choisir une autre case
                try:    
                    case_choisie=int(input('\nJoueur '+symb+' choisi une position dans la grille entre 1 et '+str((taille_reel_grille))+' : '))
                    break
                except ValueError:
                    print("Cette case n'est pas valide ! Choisi-en une autre !")
                    continue

            
            if(not(0<case_choisie<taille_reel_grille+1)):
                print("Cette case n'est pas valide ! Choisi-en une autre !")
                continue

            y=(case_choisie-1) %imax
            x=int((case_choisie-1)/imax)
            jouer(grille,x,y,imax,taille_reel_grille,L)

            if not(verification_victoire(x,y,imax,alig,grille,L)): #permet de stopper le jeu lorsque l'un des joueur gagne
                break
                
            
    print("Résultat : ")
    print("Le joueur X à gagné : "+str(compteur_x)+" fois")
    print("Le joueur O à gagné : "+str(compteur_o)+" fois") 

```

Nous avons tout d'abord une boucle for qui permet de jouer un nombre précis de parties.

Dans cette même fonction, nous demandons aux joueurs de saisir la case de leur choix. Ensuite pour éviter les erreurs nous vérifions que le choix est bien un ```int``` compris entre 1 et n (taille de la grille) et grâce à la méthode de try/except qu'il ne soit pas une ```ValueError``` (ex: ```string```). 

Ensuite, nous faisons appelle aux autres fonctions crées : construction_grille (étape 3), verification (étape 4), jouer (étape 6) verification_victoire (étape 7). 

***
***


3. Étape 3 : La construction de la grille initiale

La fonction ```construction_grille``` permet de contruire la grille du jeu initiale de maniere à être le plus lisible possible en utilisant notamment des tirets qui sépareront chaques lignes de la grille. De plus, nous avons fait le choix qu'initialement la grille allait être rempli de nombre allant de 1 à n (taille de la grille) afin que cela soit plus simple pour le choix de case des joueurs. 

```python

def contruction_grille(imax,L): #Permet de créer la grille initiale du jeu en utilisant des tiretspour une lisibilité plus optimale
    grille=[] 
    print('-----'*imax)    
    for i in range(0,imax):
        grille.append([])

        for j in range(imax):
            grille[i].append(L[j+imax*i])

        print(grille[i])
        print('-----'*imax)

    return grille

```


***
***


4. Étape 4 : La fonction ``` verification ```

La fonction ``` verification ``` permet de vérifier qu'il y a toujours des emplacements libres pour des symboles à l'intérieur de la grille. Pour cela on parcours la grille et on compare chaque éléments aux éléments de la liste L (définie plus haut) si un des éléments est égale à un élément de L la grille n'est pas encore pleine 


```python

def verification(grille,alig,imax,L): # Permet de vérifier si il y a des cases vides restantes dans la grille de jeu        
    for i in range(0,imax):
        for j in range(0,imax):
            if(grille[i][j] in L):
                return 1
    return 0
    
```    


***
***


5. Étape 5 : Le joueur choisit sa case

Ces prochaines lignes de codes nous permettent, à partir d'un numéro de case donné par le joueur, de définir ces coordonnées x et y par un  calcul trouvé par tâtonnement 

```python

case_choisie=int(input('Joueur '+symb+' choisi une position dans la grille entre 1 et '+str((taille_reel_grille))+' : '))
if(not(0<case_choisie<taille_reel_grille+1)):
    print("Cette case n'est pas dans la grille ! Choisi-en une autre !")
    continue

y=(case_choisie-1) %imax
x=int((case_choisie-1)/imax)

```


***
***


6. Étape 6 : La fonction ```jouer```

La fonction ```jouer``` nous permet de mettre à jour la grille en affichant à chaques étapes nous nouveaux symboles ajoutés. 

```python

def jouer(grille,x,y,imax,taille_reel_grille,L):
    global symb
    if (grille[x][y] in L):
        grille[x][y]=symb
        symb='X' if symb=='O' else 'O' #symbole dépend du précedent
        
        print('-----'*imax)
        for i in range(0,imax):
            print(grille[i])
            print('-----'*imax)
        
    return 1
    
```    


***
***


7. Étape 7 : La fonction ```verification_victoire```

La fonction ```verification_victoire``` permet de vérifier la grille sur ces lignes, ces colonnes ainsi que toutes ces diagonales si il a eu une victoire. Pour cela, nous créeons quatres listes de listes (ligne, colonnes, liste_diagonales1, liste_diagonales2) contenant respectivement les lignes, les colonnes et les diagonales. 

Ensuite, étant donné que les listes de lignes et colonnes possèdent des listes de mêmes taille nous utilisons la même méthode qui consiste à comparer les éléments consecutifs et de comptabiliser les éléments conécutifs et de le comparer au nombre choisi par les joueurs (alig).

Pour les diagonales, nous utilisons aussi cette methode mais uniquement lorsque la longueure de la diagonale est plus grande que l'alignement souhaité (exemple une diagonale de longueure 3 mais l'on souhaite uniquement aligner 2 symboles). Pour les diagonales de longueure égale à l'alignement souhaité nous utilisons la méthode des sets, qui permet de nous indiquer si un symbole n'apparait qu'une seule fois dans une liste (ex : on souhaite un alignement de 3 symboles avec des diagonales de longueure 3 : set(['X','O','1'])=3, set(['X','O','O'])=2 et set(['X','X','X']=1) ainsi il est plus aisé de retrouver les combinaisons gagnantes.  

```python
def verification_victoire(x,y,imax,alig,grille,L): #vérifie et annoce si il y a victoire de l'un des joueurs
    
    global compteur_o,compteur_x #Compteurs qui  permet de compter les victoires des joueurs X et O
    
    clx, clo, ccx, cco, cd1x, cd1o, cd2x, cd2o = 0, 0, 0, 0, 0, 0, 0, 0 #Compteurs qui permet de compter les symboles X et O sur les lignes, colonnes et diagonales

      
    ligne=grille #listes des lignes
    for j in range(len(ligne)):
        for i in range(len(ligne)-1):
            if ligne[j][i]==ligne[j][i+1] and ligne[j][i]=="X":
                clx+=1
            if ligne[i][j]==ligne[i+1][j] and ligne[i][j]=="O":
                clo+=1
        if clx==alig-1:
            print('X à gagné')
            compteur_x+=1
            return 0
        elif clo==alig-1:
            print('O à gané')
            compteur_o+=1
            return 0
        else:
            clx=0
            clo=0


    colonnes=[[grille[i][j] for i in range(imax)] for j in range(imax)] #listes des colonnes
    for j in range(len(colonnes)):
        for i in range(len(colonnes)-1):
            if colonnes[j][i]==colonnes[j][i+1] and colonnes[j][i]=="X":
                ccx+=1
            if colonnes[i][j]==colonnes[i+1][j] and colonnes[i][j]=="O":
                cco+=1
        if ccx==alig-1:
            print('X à gagné')
            compteur_x+=1
            return 0
        elif cco==alig-1:
            print('O à gané')
            compteur_o+=1
            return 0
        else:
            ccx=0
            cco=0




    h, w = imax, imax 
        
    liste_diagonales1=[[grille[h-1-q][p-q] for q in range(min(p, h-1), max(0, p-w+1)-1, -1)] for p in range(h+w-1)] #création d'une liste contenant liste des diagonales

    for diagonale in liste_diagonales1:
        if len(diagonale) == alig:
            unique_element = set(diagonale)
            if len(unique_element) == 1:
                elem_in_set = unique_element.pop()
                if elem_in_set=='X':
                    print("X a gagné")
                    compteur_x+=1
                    return 0
                if elem_in_set=='O':
                    print("O a gagné")
                    compteur_o+=1
                    return 0
                
        if len(diagonale) > alig:
            for i in range(len(diagonale)-2):

                if diagonale[i]=='X':
                    cd1x+=1
                if diagonale[i]=='O':
                    cd1o+=1

                if diagonale[i]==diagonale[i+1] and diagonale[i]=='X':
                    cd1x+=1
                if diagonale[i]==diagonale[i+1] and diagonale[i]=='O':
                    cd1o+=1


            if cd1x==alig:
                print("X a gagné")
                compteur_x+=1
                return 0
            elif cd1o==alig:
                print("O a gagné")
                compteur_o+=1
                return 0
            else:
                cd1o=0
                cd1x=0



    liste_diagonales2=[[grille[p - q][q] for q in range(max(p-h+1,0), min(p+1, w))] for p in range(h + w - 1)] #création d'une liste contenant liste des diagonales 

    for diagonale in liste_diagonales2:
        if len(diagonale) == alig:
            unique_element = set(diagonale)
            if len(unique_element) == 1:
                elem_in_set = unique_element.pop()
                if elem_in_set=='X':
                    print("X a gagné")
                    compteur_x+=1
                    return 0
                if elem_in_set=='O':
                    print("O a gagné")
                    compteur_o+=1
                    return 0
                
        if len(diagonale) > alig:
            for i in range(len(diagonale)-1):
                
                if diagonale[i]=='X':
                    cd2x+=1
                if diagonale[i]=='O':
                    cd2o+=1

                if diagonale[i]==diagonale[i+1] and diagonale[i]=='X':
                    cd2x+=1
                if diagonale[i]==diagonale[i+1] and diagonale[i]=='O':
                    cd2o+=1

            if cd2x==alig:
                print("X a gagné")
                compteur_x+=1
                return 0
            elif cd2o==alig:
                print("O a gagné")
                compteur_o+=1
                return 0
            else:
                cd2o=0
                cd2x=0
        

    return 1
    
``` 


***
***


8. Étape 8 : Le resultat du jeu

Ces dernières lignes de codes permettent d'afficher le resultat de partie à la fin de chaques parties.


```python

    print("Résultat : ")
    print("Le joueur X à gagné : "+str(compteur_x)+" fois")
    print("Le joueur O à gagné : "+str(compteur_o)+" fois")   

``` 

***
