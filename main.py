import sys
#dictionaries
dictsq = {"a1": "r1", "a2": "p1", "a3": "  ", "a4": "  ", "a5": "  ", "a6": "  ", "a7": "P1", "a8": "R1",
          "b1": "n1", "b2": "p2", "b3": "  ", "b4": "  ", "b5": "  ", "b6": "  ", "b7": "P2", "b8": "N1",
          "c1": "b1", "c2": "p3", "c3": "  ", "c4": "  ", "c5": "  ", "c6": "  ", "c7": "P3", "c8": "B1",
          "d1": "qu", "d2": "p4", "d3": "  ", "d4": "  ", "d5": "  ", "d6": "  ", "d7": "P4", "d8": "QU",
          "e1": "ki", "e2": "p5", "e3": "  ", "e4": "  ", "e5": "  ", "e6": "  ", "e7": "P5", "e8": "KI",
          "f1": "b2", "f2": "p6", "f3": "  ", "f4": "  ", "f5": "  ", "f6": "  ", "f7": "P6", "f8": "B2",
          "g1": "n2", "g2": "p7", "g3": "  ", "g4": "  ", "g5": "  ", "g6": "  ", "g7": "P7", "g8": "N2",
          "h1": "r2", "h2": "p8", "h3": "  ", "h4": "  ", "h5": "  ", "h6": "  ", "h7": "P8", "h8": "R2"}
dictcoor = {(0, 0): "a8", (0, 1): "b8", (0, 2): "c8", (0, 3): "d8", (0, 4): "e8", (0, 5): "f8", (0, 6): "g8", (0, 7): "h8",
            (1, 0): "a7", (1, 1): "b7", (1, 2): "c7", (1, 3): "d7", (1, 4): "e7", (1, 5): "f7", (1, 6): "g7", (1, 7): "h7",
            (2, 0): "a6", (2, 1): "b6", (2, 2): "c6", (2, 3): "d6", (2, 4): "e6", (2, 5): "f6", (2, 6): "g6", (2, 7): "h6",
            (3, 0): "a5", (3, 1): "b5", (3, 2): "c5", (3, 3): "d5", (3, 4): "e5", (3, 5): "f5", (3, 6): "g5", (3, 7): "h5",
            (4, 0): "a4", (4, 1): "b4", (4, 2): "c4", (4, 3): "d4", (4, 4): "e4", (4, 5): "f4", (4, 6): "g4", (4, 7): "h4",
            (5, 0): "a3", (5, 1): "b3", (5, 2): "c3", (5, 3): "d3", (5, 4): "e3", (5, 5): "f3", (5, 6): "g3", (5, 7): "h3",
            (6, 0): "a2", (6, 1): "b2", (6, 2): "c2", (6, 3): "d2", (6, 4): "e2", (6, 5): "f2", (6, 6): "g2", (6, 7): "h2",
            (7, 0): "a1", (7, 1): "b1", (7, 2): "c1", (7, 3): "d1", (7, 4): "e1", (7, 5): "f1", (7, 6): "g1", (7, 7): "h1"}
board = [[dictsq["a8"], dictsq["b8"], dictsq["c8"], dictsq["d8"], dictsq["e8"], dictsq["f8"], dictsq["g8"], dictsq["h8"]],
         [dictsq["a7"], dictsq["b7"], dictsq["c7"], dictsq["d7"], dictsq["e7"], dictsq["f7"], dictsq["g7"], dictsq["h7"]],
         [dictsq["a6"], dictsq["b6"], dictsq["c6"], dictsq["d6"], dictsq["e6"], dictsq["f6"], dictsq["g6"], dictsq["h6"]],
         [dictsq["a5"], dictsq["b5"], dictsq["c5"], dictsq["d5"], dictsq["e5"], dictsq["f5"], dictsq["g5"], dictsq["h5"]],
         [dictsq["a4"], dictsq["b4"], dictsq["c4"], dictsq["d4"], dictsq["e4"], dictsq["f4"], dictsq["g4"], dictsq["h4"]],
         [dictsq["a3"], dictsq["b3"], dictsq["c3"], dictsq["d3"], dictsq["e3"], dictsq["f3"], dictsq["g3"], dictsq["h3"]],
         [dictsq["a2"], dictsq["b2"], dictsq["c2"], dictsq["d2"], dictsq["e2"], dictsq["f2"], dictsq["g2"], dictsq["h2"]],
         [dictsq["a1"], dictsq["b1"], dictsq["c1"], dictsq["d1"], dictsq["e1"], dictsq["f1"], dictsq["g1"], dictsq["h1"]]]
#dictionaries

#variables
pcy, pcx = 0, 0
sqy, sqx = 0, 0
moveset = set()
whites = {"p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"}
blacks = {"P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"}
#variables

#general functions
def boardupdate():
    global board
    board = [[dictsq["a8"], dictsq["b8"], dictsq["c8"], dictsq["d8"], dictsq["e8"], dictsq["f8"], dictsq["g8"], dictsq["h8"]],
             [dictsq["a7"], dictsq["b7"], dictsq["c7"], dictsq["d7"], dictsq["e7"], dictsq["f7"], dictsq["g7"], dictsq["h7"]],
             [dictsq["a6"], dictsq["b6"], dictsq["c6"], dictsq["d6"], dictsq["e6"], dictsq["f6"], dictsq["g6"], dictsq["h6"]],
             [dictsq["a5"], dictsq["b5"], dictsq["c5"], dictsq["d5"], dictsq["e5"], dictsq["f5"], dictsq["g5"], dictsq["h5"]],
             [dictsq["a4"], dictsq["b4"], dictsq["c4"], dictsq["d4"], dictsq["e4"], dictsq["f4"], dictsq["g4"], dictsq["h4"]],
             [dictsq["a3"], dictsq["b3"], dictsq["c3"], dictsq["d3"], dictsq["e3"], dictsq["f3"], dictsq["g3"], dictsq["h3"]],
             [dictsq["a2"], dictsq["b2"], dictsq["c2"], dictsq["d2"], dictsq["e2"], dictsq["f2"], dictsq["g2"], dictsq["h2"]],
             [dictsq["a1"], dictsq["b1"], dictsq["c1"], dictsq["d1"], dictsq["e1"], dictsq["f1"], dictsq["g1"], dictsq["h1"]]]
def coordinate(pc):
    global pcy, pcx, board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == pc:
                pcy, pcx = i, j
def printboard():
    print("------------------------")
    for i in range(len(board)):
        if i>0:
            print("")
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
    print("\n------------------------")
def initialize():
    global dictsq
    global board
    print(">initialize\nOK")
    dictsq.update(a1="r1", a2="p1", a3="  ", a4="  ", a5="  ", a6="  ", a7="P1", a8="R1",
                  b1="n1", b2="p2", b3="  ", b4="  ", b5="  ", b6="  ", b7="P2", b8="N1",
                  c1="b1", c2="p3", c3="  ", c4="  ", c5="  ", c6="  ", c7="P3", c8="B1",
                  d1="qu", d2="p4", d3="  ", d4="  ", d5="  ", d6="  ", d7="P4", d8="QU",
                  e1="ki", e2="p5", e3="  ", e4="  ", e5="  ", e6="  ", e7="P5", e8="KI",
                  f1="b2", f2="p6", f3="  ", f4="  ", f5="  ", f6="  ", f7="P6", f8="B2",
                  g1="n2", g2="p7", g3="  ", g4="  ", g5="  ", g6="  ", g7="P7", g8="N2",
                  h1="r2", h2="p8", h3="  ", h4="  ", h5="  ", h6="  ", h7="P8", h8="R2")
    boardupdate()
    printboard()

def showmoves(pc):
    global pcy, pcx, sqy, sqx, board
    if pc == "p1" or pc == "p2" or pc == "p3" or pc == "p4" or pc == "p5" or pc == "p6" or pc == "p7" or pc == "p8":
        pawnforward(pc)
    elif pc == "P1" or pc == "P2" or pc == "P3" or pc == "P4" or pc == "P5" or pc == "P6" or pc == "P7" or pc == "P8":
        pawnbackward(pc)
    elif pc == "r1" or pc == "r2" or pc == "R1" or pc == "R2":
         rook(pc)
    elif pc == "b1" or pc == "b2":
        bishopforward(pc)
    elif pc == "B1" or pc == "B2":
         bishopbackward(pc)
    elif pc == "qu" or pc == "QU":
        bishopbackward(pc)
        bishopforward(pc)
        rook(pc)
    elif pc == "ki" or pc == "KI":
        king(pc)
    elif pc == "n1" or pc == "n2" or pc == "N1" or pc == "N2":
        knight(pc)
#general functions

#move functions
def pawnforward(pc):
    global pcy, pcx, board, moveset, dictcoor
    if pcy-1>0:
        submove(pcy-1, pcx, pc)
def pawnbackward(pc):
    global pcy, pcx, board, moveset, dictcoor
    if pcy+1>0:
        submove(pcy+1, pcx, pc)
def rook(pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    sqy = pcy
    sqx = pcx
    for i in range(1, 8):
         if 0<=sqy-i<=7:
            submove(sqy-i, sqx, pc)
            if board[sqy-i][sqx] != "  ":
                break
    for i in range(1, 8):
        if 0<=sqy+i<=7:
            submove(sqy+i, sqx, pc)
            if board[sqy+i][sqx] != "  ":
                break
    for i in range(1, 8):
        if 0<=sqx-i<=7:
            submove(sqy, sqx-i, pc)
            if board[sqy][sqx-i] != "  ":
                break
    for i in range(1, 8):
        if 0<=sqx+i<=7:
            submove(sqy, sqx+i, pc)
            if board[sqy][sqx+i] != "  ":
                break
def bishopforward(pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    sqy = pcy
    sqx = pcx
    for i in range(1, 8):
        if 0<=sqy-i<=7 and 0<=sqx-i<=7:
            submove(sqy-i, sqx-i, pc)
            if board[sqy-i][sqx-i] != "  ":
                break
    for i in range(1, 8):
        if 0<=sqy-i<=7 and 0<=sqx+i<=7:
            submove(sqy-i, sqx+i, pc)
            if board[sqy-i][sqx+i] != "  ":
                break
def bishopbackward(pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    sqy = pcy
    sqx = pcx
    for i in range(1, 8):
        if 0<=sqy+i<=7 and 0<=sqx+i<=7:
            submove(sqy+i, sqx+i, pc)
            if board[sqy+i][sqx+i] != "  ":
                break
    for i in range(1, 8):
        if 0<=sqy+i<=7 and 0<=sqx-i<=7:
            submove(sqy+i, sqx-i, pc)
            if board[sqy+i][sqx-i] != "  ":
                break
def king(pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0<=pcy+i<=7 and 0<=pcx+j<=7:
                submove(pcy+i, pcx+j, pc)
def knight(pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == 0 or j ==0:
                pass
            else:
                if ((i == 2 or i == -2) and (j == 1 or j == -1)) or ((i == 1 or i == -1) and (j == 2 or j == -2)) :
                    if 0<=pcy+i<=7 and 0<=pcx+j<=7:
                        submove(pcy+i, pcx+j, pc)
                elif ((i == 1 or i == -1) and (j == 1 or j == -1)) and (0<=(pcy+i)<=7 and 0<=(pcx+j)<=7) :
                    if board[pcy+i][pcx+j] == "  ":
                        moveset.add(dictcoor[(pcy+i, pcx+j)])
                else:
                    pass




#move functions

#submove functions
def submove(a, b, pc):
    global pcy, pcx, sqy, sqx, board, moveset, dictcoor
    x = pc in whites
    if 0<=a<=7 and 0<=b<=7:
         tuplex=(a, b)
         if board[a][b] == "  ":
            moveset.add(dictcoor[tuplex])
         else:
             y = board[a][b] in whites
             if x == y and x == True:
                pass
             elif x == y and x == False:
                pass
             elif x !=y and x == True:
                if board[a][b] != "KI":
                    moveset.add(dictcoor[tuplex])
             elif x !=y and x == False:
                if board[a][b] != "ki":
                    moveset.add(dictcoor[tuplex])
#submove functions

#read commands
f=open(sys.argv[1], "r")
commands=[line.split() for line in f.readlines()]
f.close()
#read commands

#execute commands
for i in range(len(commands)):
    if commands[i][0] == "print":
        print(">print")
        printboard()
    elif commands[i][0] == "initialize":
        initialize()
    elif commands[i][0] == "showmoves":
        print(">showmoves", commands[i][1])
        coordinate(commands[i][1])
        showmoves(commands[i][1])
        if moveset != set():
            for i in sorted(moveset):
                print(i, end=" ")
            print("")
            moveset.clear()
        else:
            moveset.clear()
            print("FAILED")
    elif commands[i][0] == "move":
        print(">move", commands[i][1], commands[i][2])
        coordinate(commands[i][1])
        showmoves(commands[i][1])
        if commands[i][2] in moveset:
            dictsq[dictcoor[(pcy, pcx)]] = "  "
            dictsq[commands[i][2]] = "{}".format(commands[i][1])
            moveset.clear()
            boardupdate()
            print("OK")
        else:
            moveset.clear()
            print("FAILED")
    elif commands[i][0] == "exit":
        print(">exit")
        exit()
#execute commands
