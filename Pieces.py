class pieceClass:
    #init
    def __init__(self, pieceName):
        self.pieceArray = [[]]
        self.pieceName = pieceName
        self.orientation = 0
        self.maxorientation = 1
        if self.pieceName == "T" : self.maxorientation = 3
        if self.pieceName == "Step" : self.maxorientation = 1
        if self.pieceName == "StepR" : self.maxorientation = 1
        if self.pieceName == "L" : self.maxorientation = 3
        if self.pieceName == "J" : self.maxorientation = 3
        if self.pieceName == "I" : self.maxorientation = 1
        if self.pieceName == "Box" : self.maxorientation = 0
        self.checkOrient()


    #Update pieceArray according to orientation
    def checkOrient(self) :
        if self.pieceName == "T":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [0, 1, 0]
                                  ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [0, 1],
                                    [1, 1],
                                    [0, 1]
                                  ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [0, 1, 0],
                                    [1, 1, 1]
                                  ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 1],
                                    [1, 0]
                                  ]
        if self.pieceName == "Step":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [0, 1, 1],
                                    [1, 1, 0]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 1],
                                    [0, 1]
                                    ]
        if self.pieceName == "StepR":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 0],
                                    [0, 1, 1]
                                    ]       
            if self.orientation == 1 :
                self.pieceArray = [
                                    [0, 1],
                                    [1, 1],
                                    [1, 0]
                                    ]
        if self.pieceName == "L":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [1, 0, 0]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 1],
                                    [0, 1],
                                    [0, 1]
                                    ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [0, 0, 1],
                                    [1, 1, 1]
                                    ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [1, 0],
                                    [1, 0],
                                    [1, 1]
                                    ]
        if self.pieceName == "J":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 0, 0],
                                    [1, 1, 1]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1, 1],
                                    [1, 0],
                                    [1, 0]
                                    ]
            if self.orientation == 2 :
                self.pieceArray = [
                                    [1, 1, 1],
                                    [0, 0, 1]
                                    ]
            if self.orientation == 3 :
                self.pieceArray = [
                                    [0, 1],
                                    [0, 1],
                                    [1, 1]
                                    ]
        if self.pieceName == "I":
            if self.orientation == 0 :
                self.pieceArray = [
                                    [1, 1, 1, 1, 1]
                                    ]
            if self.orientation == 1 :
                self.pieceArray = [
                                    [1],
                                    [1],
                                    [1],
                                    [1],
                                    [1]
                                    ]
        if self.pieceName == "Box":
            self.pieceArray = [
                                [1, 1],
                                [1, 1]
                                ]


    #Blits pieces and species pieceArray
    def drawer(self):
        from TetrisPieces import screen, boximg, playerX, playerY, boxSide
        for y in range(len(self.pieceArray)) :
            for x in range(len(self.pieceArray[0])) :
                if self.pieceArray[y][x] :
                    screen.blit(boximg, (playerX + x*boxSide, playerY + y*boxSide))


    #Change orientation and check if rotation is feasible
    def rotate(self) :
        import TetrisPieces
        if self.orientation == self.maxorientation : self.orientation = 0
        else : self.orientation += 1
        self.checkOrient()
        confirm = True
        if TetrisPieces.playerY + len(self.pieceArray)*TetrisPieces.boxSide > TetrisPieces.gameY or TetrisPieces.playerX + len(self.pieceArray[0])*TetrisPieces.boxSide > TetrisPieces.gameX : confirm = False
        for y in range(len(self.pieceArray)) :
            if not confirm : break
            for x in range(len(self.pieceArray[0])) :
               if self.pieceArray[y][x] and TetrisPieces.mainArray[int(TetrisPieces.playerY/TetrisPieces.boxSide) + y][int(TetrisPieces.playerX/TetrisPieces.boxSide) + x] : confirm = False
        if confirm == False :
            if self.orientation == 0 : self.orientation = self.maxorientation
            else : self.orientation -= 1
            self.checkOrient()



    #First time blit placed object and enter that in mainArray for further rounds
    def solidify(self) :
        import TetrisPieces
        for x in range(len(self.pieceArray[0])) :
            for y in range(len(self.pieceArray)) :
                if self.pieceArray[y][x] : 
                    TetrisPieces.screen.blit(TetrisPieces.placedimg, (TetrisPieces.playerX + x*TetrisPieces.boxSide, TetrisPieces.playerY + y*TetrisPieces.boxSide))
                    TetrisPieces.mainArray[int(TetrisPieces.playerY/TetrisPieces.boxSide) + y - 1][int(TetrisPieces.playerX/TetrisPieces.boxSide) + x] = True
    


    #Check if colliding with walls of game or horizontal collision with other blocks
    def collisionCheck(self) :
        import TetrisPieces
        if TetrisPieces.playerX+TetrisPieces.playerXchange+TetrisPieces.boxSide <= 0 : TetrisPieces.playerXchange = 0
        if TetrisPieces.playerX+TetrisPieces.playerXchange+(len(self.pieceArray[0]))*TetrisPieces.boxSide > TetrisPieces.gameX : TetrisPieces.playerXchange = 0
        if TetrisPieces.playerXchange < 0 and TetrisPieces.playerX+TetrisPieces.playerXchange >= 0 :
            for i in range(len(self.pieceArray)):
                x = 0
                while (self.pieceArray[i][x] == False) : x += 1
                if TetrisPieces.mainArray[int(TetrisPieces.playerY/TetrisPieces.boxSide) + i][int((TetrisPieces.playerX+TetrisPieces.playerXchange)/TetrisPieces.boxSide) + x] : TetrisPieces.playerXchange = 0
        if TetrisPieces.playerXchange > 0 and TetrisPieces.playerX+TetrisPieces.playerXchange+(len(self.pieceArray[0]))*TetrisPieces.boxSide < TetrisPieces.gameX :
            for i in range(len(self.pieceArray)):
                x = len(self.pieceArray[0]) - 1
                while (self.pieceArray[i][x] == False) : x -= 1
                if TetrisPieces.mainArray[int(TetrisPieces.playerY/TetrisPieces.boxSide) + i][int((TetrisPieces.playerX+TetrisPieces.playerXchange)/TetrisPieces.boxSide) + x] : TetrisPieces.playerXchange = 0



    #Check vertical contact
    def checker(self) :
        import TetrisPieces
        for x in range(len(self.pieceArray[0])) :
            for y in range(len(self.pieceArray)) :
                if self.pieceArray[y][x] and ((TetrisPieces.playerY + TetrisPieces.boxSide*(len(self.pieceArray)) > TetrisPieces.gameY) or TetrisPieces.mainArray[int(TetrisPieces.playerY/TetrisPieces.boxSide) + y][int(TetrisPieces.playerX/TetrisPieces.boxSide) + x]) :
                    self.solidify()
                    TetrisPieces.playerState = "PLACED"
                    return