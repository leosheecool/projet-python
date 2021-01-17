from tkinter import *	 
from tkinter import ttk



def lancement_fenetre():

    Mafenetre = Tk()
    Mafenetre.title("Morpion")
    Mafenetre.geometry('400x300')
    Mafenetre['bg']='white'

    TitreJeu  = Label(Mafenetre, text='Bienvenue dans notre jeu du Morpion') # text = chaîne à afficher
    TitreJeu.pack(padx=2, pady=5)

    ligne1 = Canvas(Mafenetre, bg='black', height=2, width=400)
    ligne1.pack()
    ligne1.create_line(0, 0, 400, 0, width=2, fill='dark blue')

    




    def Regles_jeu():
        fenetreregles = Toplevel()
        fenetreregles.title("Règles du jeu")
        fenetreregles.geometry('800x300')
        fenetreregles['bg']='salmon1'
        regle1 = Label(fenetreregles, text='VOICI LES REGLES DU JEU !')
        regle1.pack(pady=90)
        regle2 = Label(fenetreregles, text="Le but du jeu est d'aligner un certain nombre de symboles (un rond ou une croix selon) que vous aurez choisi avant de commencer' !")
        regle2.pack()
        regle3 = Label(fenetreregles, text="Ici, on joue pour la compétition, donc à la fin de toutes vos parties le score s'affiche ! Amusez-vous bien ! :)")
        regle3.pack()



    def lancement_jeu():
        cases = []

        def grille() :
            global joueur_actif, cases
            imax= zone_imax.get()
            fen=Toplevel()
            COTE=400
            MARGE = 0


            can=Canvas(fen,bg="light gray", height=COTE, width=COTE)
            can.pack()

            NB_DE_CASES=int(imax)
            PAS = COTE/NB_DE_CASES



            grille = []
            for i in range(NB_DE_CASES):
                grille.append(can.create_line(0,PAS*i,COTE,PAS*i,fill='dark green'))
                grille.append(can.create_line(PAS*i,0,PAS*i,COTE,fill='dark green'))
                

            #can.create_line(MARGE,MARGE+PAS*x,MARGE+COTE,MARGE+PAS*x,fill='black')


            cases=[ [0 for k in range(NB_DE_CASES)] for j in range(NB_DE_CASES) ]

            def left_click(event):

                global joueur_actif, n , cases
                print(cases)
                
                X = int( ((event.x ) / PAS))
                Y = int( ((event.y ) / PAS))
                print(X,Y)
                
                if (n < NB_DE_CASES**2 + 1) and (cases[X][Y] == 0):

                    if joueur_actif==1:
                        def traceCercle(X, Y):
                            r=PAS/3  #rayon                            
                            x = MARGE+PAS*(X)+ (1/2 * PAS) #coordonnées en cases à coordonnées pixels
                            y = MARGE+PAS*(Y)+ (1/2 * PAS)
                            return can.create_oval(x-r, y-r, x+r, y+r, fill='dark blue')
                        Rond = traceCercle(X,Y)
                        cases[X][Y] = -1
                        joueur_actif = 0
                        message.configure(text='Aux croix de jouer')


                    elif joueur_actif==0:
                        def traceCroix(X,Y):
                            r=PAS/3
                            x = MARGE+PAS*(X)+ (1/2 * PAS)
                            y = MARGE+PAS*(Y)+ (1/2 * PAS)
                            return can.create_line(x-r, y+r, x+r, y-r, fill='dark blue'), can.create_line(x+r, y+r, x-r, y-r, fill='dark blue')
                        Croix = traceCroix(X,Y)
                        cases[X][Y] = 1
                        joueur_actif = 1
                        message.configure(text='Aux ronds de jouer')

                    if (n >= (NB_DE_CASES + (NB_DE_CASES-1))) and (n<NB_DE_CASES**2):
                        somme = verif(cases)
                        if somme == 1 or somme == -1:
                            n = gagner(somme)
                        elif n == NB_DE_CASES**2:
                            n = gagner(0)

                    n+=1


            def verif(cases):
                """ Entrées : un tableau "carré"
                    Sorties : Calcule les sommes de chaque ligne/colonne/diagonale
                        et vérifie l'alignement."""
                sommes = [0 for k in range((NB_DE_CASES*2)+2)]
                #print(sommes)            


                # Les colonnes :
                colonnes=cases
                for k in range(NB_DE_CASES):
                    sommes[k]=sum(colonnes[k])
                

                # Les lignes :
                ligne=[[cases[i][j] for i in range(NB_DE_CASES)] for j in range(NB_DE_CASES) ]
                for k,j in zip(range(NB_DE_CASES,NB_DE_CASES*2),range(NB_DE_CASES)):
                    sommes[k] = sum(ligne[j])
                    

                # Les diagonales
                diagonale1=[cases[i][i] for i in range(NB_DE_CASES)]
                sommes[ (NB_DE_CASES*2) ] = sum(diagonale1)

                diagonale2=[cases[NB_DE_CASES-(1+i)][i] for i in range(NB_DE_CASES)]
                sommes[(NB_DE_CASES*2)+1] = sum(diagonale2)
                
                
                for i in range((NB_DE_CASES*2)+2):                     # Parcours des sommes
                    if sommes[i] == NB_DE_CASES:
                        return 1
                    elif sommes[i] == -NB_DE_CASES:
                        return -1
                return 0



            def gagner(a):
                """Cette fonction indique le gagnant en modifiant le message et en
                    renvoyant la valeur 9."""
                if a == 1:
                    message.configure(text = 'Les croix ont gagné !')
                elif a == -1:
                    message.configure(text = 'Les ronds ont gagné !')
                elif a == 0:
                    message.configure(text = 'Match nul !')
                return NB_DE_CASES**2


            def reinit():
                """Cette fonction ré-initialise les variables globales."""
                global joueur_actif, cases, n
                cases=[ [0 for k in range(NB_DE_CASES)] for j in range(NB_DE_CASES) ]
                joueur_actif = 0          
                n = 1

                message.configure(text='Aux croix de jouer')
                can.delete(ALL)      # Efface toutes les figures
                grille = []
                for i in range(NB_DE_CASES):
                    grille.append(can.create_line(0,PAS*i,COTE,PAS*i,fill='dark green'))
                    grille.append(can.create_line(PAS*i,0,PAS*i,COTE,fill='dark green'))




            message=Label(fen, text='Aux croix de jouer')
            message.pack(padx=3, pady=3)


            bouton_quitter = Button(fen, text='Quitter', command=Mafenetre.destroy)
            bouton_quitter.pack(padx=3, pady=3, side='right') 

            bouton_reload = Button(fen, text='Recommencer', command=reinit)
            bouton_reload.pack(padx=3, pady=3, side='left')





            can.bind('<Button-1>', left_click)
        
        
        
        
        
        


        fenetrejeu =  Toplevel()
        fenetrejeu.title("Morpion")
        fenetrejeu['bg']='navajo white'

        debut = Label(fenetrejeu, text='Avant de commencer !')
        debut.pack(pady=50)

        zone1 = Frame(fenetrejeu, bg='ivory3')

        choix_imax = Label(zone1, text='Choisi la taille de la grille qui est donc le nombre de symbole que tu devras aligner pour gagner la partie !')
        choix_imax.pack()

        zone_imax = Entry(zone1)
        zone_imax.pack()

        
        zone1.pack(fill=X, ipady=5, padx=10,pady=10)



        BoutonCommencer = Button(fenetrejeu, text = 'Commencer', command=grille)
        BoutonCommencer.pack(pady=50)

        BoutonQuitter = Button(fenetrejeu, text='Quitter',bg='pink', fg='white', command=Mafenetre.destroy)
        BoutonQuitter.pack(side='bottom')

        



    BoutonRegles = Button(Mafenetre, text="Les règles du jeu !", command=Regles_jeu)
    BoutonRegles.pack(side='left')

    BoutonJouer = Button(Mafenetre, text="C'est partie !", command=lancement_jeu)
    BoutonJouer.pack(side='right')


    BoutonQuitter = Button(Mafenetre, text='Quitter',bg='pink', fg='white', command=Mafenetre.destroy)
    BoutonQuitter.pack(side='bottom')
    
    ligne2 = Canvas(Mafenetre, bg='black', height=2, width=400)
    ligne2.pack()
    ligne2.create_line(0, 0, 400, 0, width=2, fill='dark blue')
    


        
    Mafenetre.mainloop()











if __name__ == '__main__':

    

    joueur_actif=0
    n=1 #nb de tour de jeu
    
    lancement_fenetre()