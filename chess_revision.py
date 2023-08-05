#create a board of nested lists
#Suck dick right there mate
def main():
    #create a board of nested lists
    board=[["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"],
           ["?","?","?","?","?","?","?","?"]]
#implement the white piece
    x, w= input("Piece and position?").split(" ")
    ppiece=white(x)
    y=w[0]
    w=w[1]
    y= column(y)
    w= line(w)
    board[w][y]= ppiece

#implement black pieces whith a while loop
    black_pieces=0
    while black_pieces<16:
        #print it in a way that looks like a chess boards and lets you see where your piece is in the board
        print (board[0],board[1], board[2], board[3],board[4], board[5], board[6], board[7] ,sep='\n')
        eb = input("What enemies are in the board?")
        #this ends the loop with the word done
        if "done" in eb:
            if black_pieces < 1:
                continue
            elif black_pieces >= 1:
                black_pieces= black_pieces + 16
    #this adds the pieces to the board
        else:
            ex,ew=eb.split(" ")
            ey=ew[0]
            ew=ew[1]
            epiece=black(ex)
            if board[line(ew)][column(ey)]=="?":
                board[line(ew)][column(ey)]= epiece
                black_pieces= black_pieces + 1
                #this next line avoids you putting two pieces in the same spot
            else:
                print("already a piece there")
    #prints the board after you finish putting your enemy pieces in it
    #checks for the piece you played
    try:
        if board[w][y]== "k":
            #checks all the king attack movements so he can tell you where he can atack
            if board[w][add1(y)] != "?":
                print("your king may conquer the", black_piece(board[w][add1(y)]), "to his right")
            if board[w][sub1(y)] != "?":
                print("your king may conquer the", black_piece(board[w][sub1(y)]), "to his left")
            if board[sub1(w)][y] != "?":
                print ("your king may conquer the", black_piece(board[sub1(w)][y]), "in front of him")
            if board[add1(w)][y] != "?":
                print ("your king may conquer the", black_piece(board[add1(w)][y]), "in  his back")
            if board[add1(w)][sub1(y)] != "?":
                print ("your king may conquer the", black_piece(board[add1(w)][sub1(y)]), "in the downleft diagonal")
            if board[add1(w)][add1(y)] != "?":
                print ("your king may conquer the", black_piece(board[add1(w)][add1(y)]), "in the downright diagonal")
            if board[sub1(w)][sub1(y)] != "?":
                print ("your king may conquer the", black_piece(board[sub1(w)][sub1(y)]), "in the upperleft diagonal")
            if board[sub1(w)][add1(y)] != "?":
                print ("your king may conquer the", black_piece(board[sub1(w)][add1(y)]), "in the upperright diagonal")
        elif board[w][y]== "p":
            if board[sub1(w)][sub1(y)] != "?":
                print ("your pawn may conquer the", black_piece(board[sub1(w)][sub1(y)]), "in the upperleft diagonal")
            if board[sub1(w)][add1(y)] != "?":
                print ("your pawn may conquer the", black_piece(board[sub1(w)][add1(y)]), "in the upperright diagonal")
    #in case the piece is in one of the borders so we dont have an error
    except IndexError:
            pass
#used to add 1 to every int
def add1(x):
    x = x+1
    return x
#used to subtract 1 to the int
def sub1(x):
    x= x-1
    return x
#convertes letters into numbers to the index of the columns
def column(x):
    if x=="a":
        return 0
    elif x=="b":
        return 1
    elif x=="c":
        return 2
    elif x=="d":
        return 3
    elif x=="e":
        return 4
    elif x=="f":
        return 5
    elif x=="g":
        return 6
    elif x=="h":
        return 7
#adjust the numbers in a rtegular chess board to the index of the lists
def line(x):
    if x=="8":
        return 0
    elif x=="7":
        return 1
    elif x=="6":
        return 2
    elif x=="5":
        return 3
    elif x=="4":
        return 4
    elif x=="3":
        return 5
    elif x=="2":
        return 6
    elif x=="1":
        return 7
#defines your pieces and tells what to put in the board
def white(x):
    if x == "king":
        return "k"
    elif x== "pawn":
        return "p"
    else:
        print("Piece not found")
#same as white but it defines the black pieces
def black(x):
    if x=="pawn":
        return "P"
    elif x=="rook":
        return "R"
    elif x=="knight":
        return "H"
    elif x=="bishop":
        return "B"
    elif x=="queen":
        return "Q"
    elif x=="king":
        return  "K"
#receives the conbverted from the previous function and returns them to
#the original formate, used to print what pieces you may eat
def black_piece(x):
    if x=="P":
        return "pawn"
    elif x=="R":
        return "rook"
    elif x=="H":
        return "knight"
    elif x=="B":
        return "bishop"
    elif x=="Q":
        return "queen"
    elif x=="K":
        return  "king"

main()