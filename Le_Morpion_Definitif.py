


class fonctions_utiles_class:

    
    def contruction_grille(self,imax,L): #Permet de créer la grille initiale du jeu en utilisant des tirets et des barres verticales pour une lisibilité plus optimale
        
        """Construit la grille initiale.

        Args:
            imax : taille de la grille
            L : liste des nombres de 1 à imax²

        Returns:    
            grille : grille initiale
        
        >>> imax = 3
        
        >>> L = [1, 2, 3, 4, 5, 6, 7, 8]

        >>> grille = construction_grille(imax,L)

        >>> grille
        ---------------
        [1, 2, 3]
        ---------------
        [4, 5, 6]
        ---------------
        [7, 8, 9]
        ---------------
        """
        
        grille=[] 
        print('-----'*imax)    
        for i in range(0,imax):
            grille.append([])

            for j in range(imax):
                grille[i].append(L[j+imax*i])

            print(grille[i])
            print('-----'*imax)

        return grille




    def verification(self,grille,alig,imax,L): # Permet de vérifier si il y a des cases vides restantes dans la grille de jeu
        
        """Vérifie qu'il reste des cases vides dans la grille.

        Args:
            grille : grille de jeu
            alig : nombre de symbole à aligner pour remporter la partie
            imax : taille de la grille
            L : liste des nombres de 1 à imax²

        Returns:    
            1 : si il reste des cases vide
            0 : si la grille est pleine

        >>> imax = 3

        >>> alig = 3

        >>> L = [1, 2, 3, 4, 5, 6, 7, 8]
        
        >>> grille1 =
        ---------------
        [1, 2, 3]
        ---------------
        [4, 5, 6]
        ---------------
        [7, 8, 9]
        ---------------

        >>> verification(grille1,alig,imax,L)
        1

        >>> grille2 =
        ---------------
        [X, O, X]
        ---------------
        [X, O, X]
        ---------------
        [O, X, O]
        ---------------

        >>> verification(grille2,alig,imax,L)
        0
        """
            
        for i in range(0,imax):
            for j in range(0,imax):
                if(grille[i][j] in L):
                    return 1
        return 0





    def verification_victoire(self,x,y,imax,alig,grille,L): #vérifie et annoce si il y a victoire de l'un des joueurs

        """Vérifie qu'il y a une victoire sur une ligne, une colonne ou une diagonale.

        Args:
            
            x : coordonnée colonne de l'emplacement choisi par le joueur
            y : coordonnée ligne de l'emplacement choisi par le joueur
            alig : nombre de symbole à aligner pour remporter la partie
            grille : grille de jeu
            L : liste des nombres de 1 à imax²

        Returns:    
            1 : si il n'y a pas encore de victoire
            0 : si il y a une victoire
        """
        
        
        
        
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
                print('X à gagné\n')
                compteur_x+=1
                return 0
            elif clo==alig-1:
                print('O à gané\n')
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
                print('X à gagné\n')
                compteur_x+=1
                return 0
            elif cco==alig-1:
                print('O à gané\n')
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
                        print("X a gagné\n")
                        compteur_x+=1
                        return 0
                    if elem_in_set=='O':
                        print("O a gagné\n")
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
                    print("X a gagné\n")
                    compteur_x+=1
                    return 0
                elif cd1o==alig:
                    print("O a gagné\n")
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
                        print("X gagne\n")
                        compteur_x+=1
                        return 0
                    if elem_in_set=='O':
                        print("O gagne\n")
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
                    print("X gagne\n")
                    compteur_x+=1
                    return 0
                elif cd2o==alig:
                    print("O gagne\n")
                    compteur_o+=1
                    return 0
                else:
                    cd2o=0
                    cd2x=0
            

        return 1




    def jouer(self,grille,x,y,imax,taille_reel_grille,L): #permet de mettre le symbole à l'emplacement choisi par le joueur si ce dernier est vide
        
        """Place le symbole à l'emplacement choisi par le joueur si cette case est vide.

        Args:
            grille : grille de jeu
            x : coordonnée colonne de l'emplacement choisi par le joueur
            y : coordonnée ligne de l'emplacement choisi par le joueur
            imax : taille de la grille
            taille_reel_grille : taille de la grille réel (=imax²)
            L : liste des nombres de 1 à imax²

        Returns:    
            retourne la grille qui a été mise à jour.

        >>> x = 3

        >>> y = 1

        >>> imax = 3

        >>> taille_reel_grille = 9

        >>> L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> grille =
        ---------------
        [1, 2, 3]
        ---------------
        [4, 5, 6]
        ---------------
        [7, 8, 9]
        ---------------
        
        >>> jouer(grille,x,y,imax,taille_reel_grille,L)
        ---------------
        [1, 2, 3]
        ---------------
        [4, 5, X]
        ---------------
        [7, 8, 9]
        ---------------
        """
        
        global symb
        #symb=MaClass.symb
        

        if (grille[x][y] in L):
            grille[x][y]=symb
            symb='X' if symb=='O' else 'O' #symbole dépend du précedent
            
            print('-----'*imax)
            for i in range(0,imax):
                print(grille[i])
                print('-----'*imax)
            
        return 1






class jeu_principal_class :

    def jeu(self,imax,taille_reel_grille,alig,nombre_partie_a_jouer,L):
        
        """Démarre le jeu et affiche le résultat à la fin de la partie.

        Args:
            imax : taille de la grille
            taille_reel_grille : taille de la grille réel (=imax²)
            alig : nombre de symbole à aligner pour remporter la partie
            nombre_partie_a_jouer : le nombre de partie à jouer
            L : liste des nombres de 1 à imax²

        Returns:    
            Affiche à l'écran le résultat de la partie.
        """
        
        
        global symb
        
        for k in range(nombre_partie_a_jouer): #permet de jouer un certain nombre de partie
            print('\nPartie '+str(k+1)+ ' :')
            grille=fonctions_utiles.contruction_grille(imax,L) #construction de la grille de taille imax
            while (fonctions_utiles.verification(grille,alig,imax,L)): #tant qu'il y a des cases vides
                    
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
                fonctions_utiles.jouer(grille,x,y,imax,taille_reel_grille,L)

                if not(fonctions_utiles.verification_victoire(x,y,imax,alig,grille,L)): #permet de stopper le jeu lorsque l'un des joueur gagne
                    break
            
                    
                
        print("Résultats : ")
        print("Le joueur X à gagné : "+str(compteur_x)+" fois")
        print("Le joueur O à gagné : "+str(compteur_o)+" fois\n")            
      






if __name__ == '__main__':

    fonctions_utiles=fonctions_utiles_class()
    jeu_principal=jeu_principal_class()

    input('\nBienvenue dans LE MEILLEUR jeu du Morpion ! Es-tu prêt ? (Oui ou Oui ?) : ')
    imax = int(input('\nChoisi une taille de grille : ')) 
    taille_reel_grille = imax**2 #taille 2D de la grille
    L=[j for j in range(1,taille_reel_grille+1)] 
    alig=int(input('\nDifficulté : Choisi un nombre de symbole à aligner dans la grille : ')) 

    nombre_partie_a_jouer=int(input('\nCombien de partie voulez vous jouer ? : '))

    symb='X' #symbole du premier joueur

    compteur_x=0 #Compteurs qui  permet de compter les victoires du joueurs X
    compteur_o=0 #Compteurs qui  permet de compter les victoires du joueurs O

    jeu_principal.jeu(imax,taille_reel_grille,alig,nombre_partie_a_jouer,L)
      