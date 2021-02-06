#!/user/bin/python3.7
from victoyManagement import CheckVictory

class Game():
    def __init__(self):
        self.tab = []
        self.tabSize = 0
        self.actualPlayer = 0
        self.symbol = ["X", "O"]
        self.check = CheckVictory()

        self.getNumberValues()
        self.initGame()

    def getNumberValues(self):
        while (self.tabSize <= 0):
            try:
                self.tabSize = int(input("Choisi une taille de grille : "))
            except Exception as e:
                print("Entre un nombre valide")

    def initGame(self):
        for _ in range(self.tabSize):
            self.tab.append([' ' for _ in range(self.tabSize)])
        self.mainLoop()

    def printTab(self):
        nb = 1

        for i in range(1, self.tabSize + 1):
            print(" " + str(i), end="")
        print('')
        for row in self.tab:
            print("--" * len(row) + "-")
            print("|", end="")
            for col in row:
                print(col + "|", end="")
            print(" " + str(nb))
            nb += 1
        print("--" * len(row) + "-")

    def manageUserInput(self):
        row, col = 0, 0

        while True:
            while row <= 0 or row > len(self.tab):
                try:
                    row = int(input("Choisi la ligne: "))
                except Exception as e:
                    print("Entre un nombre valide")
            while col <= 0 or col > len(self.tab):
                try:
                    col = int(input("Choisi la colonne: "))
                except Exception as e:
                    print("Entre un nombre valide")

            if self.tab[row - 1][col - 1] == ' ':
                self.tab[row - 1][col - 1] = self.symbol[self.actualPlayer]
                break
            else:
                print("La case est déjà prise")
                row, col = 0, 0

    def manageVictory(self):
        val = self.check.checkWin(self.tab)
        if val != " ":
            self.printTab()
            print(val + " gagne la partie!")
            return True
        return False

    def mainLoop(self):
        while(True):
            self.printTab()
            print("Au tour de " + self.symbol[self.actualPlayer])
            self.manageUserInput()
            if self.manageVictory():
                break
            self.actualPlayer = 1 if self.actualPlayer == 0 else  0


Game()