
def main():
#board
    a1 ="?"
    a2="?"
    a3="?"
    a4="?"
    a5="?"
    a6="?"
    a7="?"
    a8="?"
    b1="?"
    b2="?"
    b3="?"
    b4="?"
    b5="?"
    b6="?"
    b7="?"
    b8="?"
    c1="?"
    c2="?"
    c3="?"
    c4="?"
    c5="?"
    c6="?"
    c7="?"
    c8="?"
    d1="?"
    d2="?"
    d3="?"
    d4="?"
    d5="?"
    d6="?"
    d7="?"
    d8="?"
    e1="?"
    e2="?"
    e3="?"
    e4="?"
    e5="?"
    e6="?"
    e7="?"
    e8="?"
    f1="?"
    f2="?"
    f3="?"
    f4="?"
    f5="?"
    f6="?"
    f7="?"
    f8="?"
    g1="?"
    g2="?"
    g3="?"
    g4="?"
    g5="?"
    g6="?"
    g7="?"
    g8="?"
    h1="?"
    h2="?"
    h3="?"
    h4="?"
    h5="?"
    h6="?"
    h7="?"
    h8="?"
    top_board= a8, b8, c8, d8,e8,f8,g8,h8 , a7, b7, c7, d7,e7,f7,g7,h7, a6, b6, c6, d6,e6,f6,g6,h6, a5, b5, c5, d5,e5,f5,g5,h5,
    totop_board= a8, b8, c8, d8,e8,f8,g8,h8 , a7, b7, c7, d7,e7,f7,g7,h7
    big_8= a8, b8, c8, d8,e8,f8,g8,h8
    big_7= a7, b7, c7, d7,e7,f7,g7,h7
    lotop_board= a6, b6, c6, d6, e6, f6, g6, h6, a5, b5, c5, d5,e5,f5,g5,h5
    big_6= a6, b6, c6, d6,e6,f6,g6,h6
    big_5= a5, b5, c5, d5,e5,f5,g5,h5
    bottom_board= a4, b4, c4, d4,e4,f4,g4,h4, a3, b3, c3, d3,e3,f3,g3,h3, a2, b2, c2, d2,e2,f2,g2,h2, a1, b1, c1, d1,e1,f1,g1,h1
    tobottom_board= a4, b4, c4, d4,e4,f4,g4,h4, a3, b3, c3, d3,e3,f3,g3,h3
    big_4=a4, b4, c4, d4,e4,f4,g4,h4
    big_3=a3, b3, c3, d3,e3,f3,g3,h3
    lobottom_board=a2, b2, c2, d2,e2,f2,g2,h2, a1, b1, c1, d1,e1,f1,g1,h1
    big_2=a2, b2, c2, d2,e2,f2,g2,h2
    big_1=a1, b1, c1, d1,e1,f1,g1,h1
    print('\n',"8", a8, b8, c8, d8,e8,f8,g8,h8 ,'\n',"7", a7, b7, c7, d7,e7,f7,g7,h7,'\n',"6", a6, b6, c6, d6,e6,f6,g6,h6,'\n',"5", a5, b5, c5, d5,e5,f5,g5,h5,'\n',"4", a4, b4, c4, d4,e4,f4,g4,h4,'\n',"3", a3, b3, c3, d3,e3,f3,g3,h3,'\n',"2", a2, b2, c2, d2,e2,f2,g2,h2,'\n',"1", a1, b1, c1, d1,e1,f1,g1,h1,'\n'," ", "a", "b", "c", "d","e","f","g","h")
    x, y= input("Piece and position?").split(" ")
    ppiece=white(x)
    if y=="a1":
        a1= ppiece
    elif y=="a2":
        a2= ppiece
    elif y=="a3":
        a3= ppiece
    elif y=="a4":
        a4= ppiece
    elif y=="a5":
        a5= ppiece
    elif y=="a6":
        a6= ppiece
    elif y=="a7":
        a7= ppiece
    elif y=="a8":
        a8= ppiece
    elif y=="b1":
        b1= ppiece
    elif y=="b2":
        b2= ppiece
    elif y=="b3":
        b3= ppiece
    elif y=="b4":
        b4= ppiece
    elif y=="b5":
        b5= ppiece
    elif y=="b6":
        b6= ppiece
    elif y=="b7":
        b7= ppiece
    elif y=="b8":
        b8= ppiece
    elif y=="c1":
        c2= ppiece
    elif y=="c2":
        c2= ppiece
    elif y=="c2":
        c2= ppiece
    elif y=="c3":
        c3= ppiece
    elif y=="c4":
        c4= ppiece
    elif y=="c5":
        c5= ppiece
    elif y=="c6":
        c6= ppiece
    elif y=="c7":
        c7= ppiece
    elif y=="c8":
        c8= ppiece
    elif y=="d1":
        d1= ppiece
    elif y=="d2":
        d2= ppiece
    elif y=="d3":
        d3= ppiece
    elif y=="d4":
        d4= ppiece
    elif y=="d5":
        d5= ppiece
    elif y=="d6":
        d6= ppiece
    elif y=="d7":
        d7= ppiece
    elif y=="d8":
        d8= ppiece
    elif y=="e1":
        e1= ppiece
    elif y=="e2":
        e2= ppiece
    elif y=="e3":
        e3= ppiece
    elif y=="e4":
        e4= ppiece
    elif y=="e5":
        e5= ppiece
    elif y=="e6":
        e6= ppiece
    elif y=="e7":
        e7= ppiece
    elif y=="e8":
        e8= ppiece
    elif y=="f1":
        f1= ppiece
    elif y=="f2":
        f2= ppiece
    elif y=="f3":
        f3= ppiece
    elif y=="f4":
        f4= ppiece
    elif y=="f5":
        f5= ppiece
    elif y=="f6":
        f6= ppiece
    elif y=="f7":
        f7= ppiece
    elif y=="f8":
        f8= ppiece
    elif y=="g1":
        g1= ppiece
    elif y=="g2":
        g2= ppiece
    elif y=="g3":
        g3= ppiece
    elif y=="g4":
        g4= ppiece
    elif y=="g5":
        g5= ppiece
    elif y=="g6":
        g6= ppiece
    elif y=="g7":
        g7= ppiece
    elif y=="g8":
        g8= ppiece
    elif y=="h1":
        h1= ppiece
    elif y=="h2":
        h2= ppiece
    elif y=="h3":
        h3= ppiece
    elif y=="h4":
        h4= ppiece
    elif y=="h5":
        h5= ppiece
    elif y=="h6":
        h6= ppiece
    elif y=="h7":
        h7= ppiece
    elif y=="h8":
        h8= ppiece
    black_pieces=0
    print('\n',"8", a8, b8, c8, d8,e8,f8,g8,h8 ,'\n',"7", a7, b7, c7, d7,e7,f7,g7,h7,'\n',"6", a6, b6, c6, d6,e6,f6,g6,h6,'\n',"5", a5, b5, c5, d5,e5,f5,g5,h5,'\n',"4", a4, b4, c4, d4,e4,f4,g4,h4,'\n',"3", a3, b3, c3, d3,e3,f3,g3,h3,'\n',"2", a2, b2, c2, d2,e2,f2,g2,h2,'\n',"1", a1, b1, c1, d1,e1,f1,g1,h1,'\n'," ", "a", "b", "c", "d","e","f","g","h")
#while loop to put the necessary black pieces
    while black_pieces<16:
        print('\n',"8", a8, b8, c8, d8,e8,f8,g8,h8 ,'\n',"7", a7, b7, c7, d7,e7,f7,g7,h7,'\n',"6", a6, b6, c6, d6,e6,f6,g6,h6,'\n',"5", a5, b5, c5, d5,e5,f5,g5,h5,'\n',"4", a4, b4, c4, d4,e4,f4,g4,h4,'\n',"3", a3, b3, c3, d3,e3,f3,g3,h3,'\n',"2", a2, b2, c2, d2,e2,f2,g2,h2,'\n',"1", a1, b1, c1, d1,e1,f1,g1,h1,'\n'," ", "a", "b", "c", "d","e","f","g","h")
        w= input("What enemies need death??")
        if "done" in w:
            if black_pieces < 1:
                continue
            elif black_pieces >= 1:
                black_pieces= black_pieces + 16
        elif  "done" not in w:
            x,y=w.split(" ")
            if x=="pawn" or x=="king" or x== "rook" or x== "bishop" or x=="queen" or x=="knight":
                epiece=black(x)
                if y=="a1" and a1 =="?":
                    a1= epiece
                    black_pieces= black_pieces +1
                elif y=="a2" and a2 =="?":
                    a2= epiece
                    black_pieces= black_pieces +1
                elif y=="a3" and a3 =="?":
                    a3= epiece
                    black_pieces= black_pieces +1
                elif y=="a4" and a4 =="?":
                    a4= epiece
                    black_pieces= black_pieces +1
                elif y=="a5" and a5 =="?":
                    a5= epiece
                    black_pieces= black_pieces +1
                elif y=="a6" and a6 =="?":
                    a6= epiece
                    black_pieces= black_pieces +1
                elif y=="a7" and a7 =="?":
                    a7= epiece
                    black_pieces= black_pieces +1
                elif y=="a8" and a8 =="?":
                    a8= epiece
                    black_pieces= black_pieces +1
                elif y=="b1" and b1 =="?":
                    b1= epiece
                    black_pieces= black_pieces +1
                elif y=="b2" and b2 =="?":
                    b2= epiece
                    black_pieces= black_pieces +1
                elif y=="b3" and b3 =="?":
                    b3= epiece
                    black_pieces= black_pieces +1
                elif y=="b4" and b4 =="?":
                    b4= epiece
                    black_pieces= black_pieces +1
                elif y=="b5" and b5 =="?":
                    b5= epiece
                    black_pieces= black_pieces +1
                elif y=="b6" and b6 =="?":
                    b6= epiece
                    black_pieces= black_pieces +1
                elif y=="b7" and b7 =="?":
                    b7= epiece
                    black_pieces= black_pieces +1
                elif y=="b8" and b8 =="?":
                    b8= epiece
                    black_pieces= black_pieces +1
                elif y=="c1" and c1 =="?":
                    c1= epiece
                    black_pieces= black_pieces +1
                elif y=="c2" and c2 =="?":
                    c2= epiece
                    black_pieces= black_pieces +1
                elif y=="c3" and c3 =="?":
                    c3= epiece
                    black_pieces= black_pieces +1
                elif y=="c4" and c4 =="?":
                    c4= epiece
                    black_pieces= black_pieces +1
                elif y=="c5" and c5 =="?":
                    c5= epiece
                    black_pieces= black_pieces +1
                elif y=="c6" and c6 =="?":
                    c6= epiece
                    black_pieces= black_pieces +1
                elif y=="c7" and c7 =="?":
                    c7= epiece
                    black_pieces= black_pieces +1
                elif y=="c8" and c8 =="?":
                    c8= epiece
                    black_pieces= black_pieces +1
                elif y=="d1" and d1 =="?":
                    d1= epiece
                    black_pieces= black_pieces +1
                elif y=="d2" and d2 =="?":
                    d2= epiece
                    black_pieces= black_pieces +1
                elif y=="d3" and d3 =="?":
                    d3= epiece
                    black_pieces= black_pieces +1
                elif y=="d4" and d4 =="?":
                    d4= epiece
                    black_pieces= black_pieces +1
                elif y=="d5" and d5 =="?":
                    d5= epiece
                    black_pieces= black_pieces +1
                elif y=="d6" and d6 =="?":
                    d6= epiece
                    black_pieces= black_pieces +1
                elif y=="d7" and d7 =="?":
                    d7= epiece
                    black_pieces= black_pieces +1
                elif y=="d8" and d8 =="?":
                    d8= epiece
                    black_pieces= black_pieces +1
                elif y=="e1" and e1 =="?":
                    e1= epiece
                    black_pieces= black_pieces +1
                elif y=="e2" and e2 =="?":
                    e2= epiece
                    black_pieces= black_pieces +1
                elif y=="e3" and e3 =="?":
                    e3= epiece
                    black_pieces= black_pieces +1
                elif y=="e4" and e4 =="?":
                    e4= epiece
                    black_pieces= black_pieces +1
                elif y=="e5" and e5 =="?":
                    e5= epiece
                    black_pieces= black_pieces +1
                elif y=="e6" and e6 =="?":
                    e6= epiece
                    black_pieces= black_pieces +1
                elif y=="e7" and e7 =="?":
                    e7= epiece
                    black_pieces= black_pieces +1
                elif y=="e8" and e8 =="?":
                    e8= epiece
                    black_pieces=black_pieces +1
                elif y=="f1" and f1 =="?":
                    f1= epiece
                    black_pieces= black_pieces +1
                elif y=="f2" and f2 =="?":
                    f2= epiece
                    black_pieces= black_pieces +1
                elif y=="f3" and f3 =="?":
                    f3= epiece
                    black_pieces= black_pieces +1
                elif y=="f4" and f4 =="?":
                    f4= epiece
                    black_pieces= black_pieces +1
                elif y=="f5" and f5 =="?":
                    f5= epiece
                    black_pieces= black_pieces +1
                elif y=="f6" and f6 =="?":
                    f6= epiece
                    black_pieces= black_pieces +1
                elif y=="f7" and f7 =="?":
                    f7= epiece
                    black_pieces= black_pieces +1
                elif y=="f8" and f8 =="?":
                    f8= epiece
                    black_pieces= black_pieces +1
                elif y=="g1" and g1 =="?":
                    g1= epiece
                    black_pieces= black_pieces +1
                elif y=="g2" and g2 =="?":
                    g2= epiece
                    black_pieces= black_pieces +1
                elif y=="g3" and g3 =="?":
                    g3= epiece
                    black_pieces= black_pieces +1
                elif y=="g4" and g4 =="?":
                    g4= epiece
                    black_pieces= black_pieces +1
                elif y=="g5" and g5 =="?":
                    g5= epiece
                    black_pieces= black_pieces +1
                elif y=="g6" and g6 =="?":
                    g6= epiece
                    black_pieces= black_pieces +1
                elif y=="g7" and g7 =="?":
                    g7= epiece
                    black_pieces= black_pieces +1
                elif y=="g8" and g8 =="?":
                    g8= epiece
                    black_pieces= black_pieces +1
                elif y=="h1" and h1 =="?":
                    h1= epiece
                    black_pieces= black_pieces +1
                elif y=="h2" and h2 =="?":
                    h2= epiece
                    black_pieces= black_pieces +1
                elif y=="h3" and h3 =="?":
                    h3= epiece
                    black_pieces= black_pieces +1
                elif y=="h4" and h4 =="?":
                    h4= epiece
                    black_pieces= black_pieces +1
                elif y=="h5" and h5 =="?":
                    h5= epiece
                    black_pieces= black_pieces +1
                elif y=="h6" and h6 =="?":
                    h6= epiece
                    black_pieces= black_pieces +1
                elif y=="h7" and h7 =="?":
                    h7= epiece
                    black_pieces= black_pieces +1
                elif y=="h8" and h8 =="?":
                    h8= epiece
                    black_pieces= black_pieces +1

    if "p" or "k" in top_board:
        if "p" in a8 or "p" in b8 or "p" in c8 or "p" in d8 or "p" in e8 or "p" in f8 or "p" in g8 or "p" in h8:
            print("your pawn should transform into other piece of your choosing")
        elif "k" in a8:
            if  "?" not in b8:
                print ("your king may conquer the ", black_piece(b8)," in b8")
            if "?"not in a7:
                print ("your king may conquer the ", black_piece(a7)," in a7")
            if "?"not in b7:
                print ("your king may conquer the " , black_piece(b7)," in b7")
        elif "k" in b8:
            if "?"not in a8:
                print ("your king may conquer the ", black_piece(a8)," in a8")
            if "?"not in c8  :
                print ("your king may conquer the ", black_piece(c8)," in c8")
            if "?"not in a7  :
                print ("your king may conquer the ", black_piece(a7)," in a7")
            if "?"not in b7 :
                print ("your king may conquer the ", black_piece(b7)," in b7")
            if "?"not in c7 :
                print ("your king may conquer the ", black_piece(c7)," in c7")
        elif "k" in c8:
            if "?"not in b8:
                print ("your king may conquer the " ,black_piece(b8)," in b8")
            if "?"not in d8 :
                print ("your king may conquer the ", black_piece(d8)," in d8")
            if "?"not in d7:
                print ("your king may conquer the " ,black_piece(d7)," in d7")
            if "?"not in b7:
                print ("your king may conquer the " ,black_piece(b7)," in b7")
            if "?"not in c7 :
                print ("your king may conquer the " ,black_piece(c7)," in c7")
        elif "k" in d8:
            if "?"not in c8:
                print ("your king may conquer the " ,black_piece(c8)," in c8")
            if "?"not in e8 :
                print ("your king may conquer the " ,black_piece(e8)," in e8")
            if "?"not in d7:
                print ("your king may conquer the " ,black_piece(d7)," in d7")
            if "?"not in e7:
                print ("your king may conquer the " ,black_piece(e7)," in e7")
            if "?"not in c7 :
                print ("your king may conquer the ", black_piece(c7)," in c7")
        elif "k" in e8:
            if "?"not in f8:
                print ("your king may conquer the " ,black_piece(f8)," in f8")
            if "?"not in d8:
                print ("your king may conquer the ", black_piece(d8)," in d8")
            if "?"not in d7:
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in e7:
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in f7 :
                print ("your king may conquer the ", black_piece(f7)," in f7")
        elif "k" in f8:
            if "?"not in g8:
                print ("your king may conquer the " ,black_piece(g8)," in g8")
            if "?"not in e8:
                print ("your king may conquer the ", black_piece(e8)," in e8")
            if "?"not in g7:
                print ("your king may conquer the ", black_piece(g7)," in g7")
            if "?"not in e7:
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in f7 :
                print ("your king may conquer the ", black_piece(f7)," in f7")
        elif "k" in g8:
            if "?"not in h8:
                print ("your king may conquer the " ,black_piece(h8)," in h8")
            if "?"not in h7 :
                print ("your king may conquer the ", black_piece(h7)," in h7")
            if "?"not in g7:
                print ("your king may conquer the ", black_piece(g7)," in g7")
            if "?"not in f8:
                print ("your king may conquer the ", black_piece(f8)," in f8")
            if "?"not in f7 :
                print ("your king may conquer the ", black_piece(f7)," in f7")
        elif "k" in h8:
            if "?"not in h7 :
                print ("your king may conquer the ", black_piece(h7)," in h7")
            if "?"not in g7:
                print ("your king may conquer the ", black_piece(g7)," in g7")
            if "?"not in g8:
                print ("your king may conquer the ", black_piece(g8)," in g8")
        elif "p" in a7:
            if "?"not in b8 :
                print ("your pawn may conquer the " ,black_piece(b8)," in b8")
        elif "k" in a7:
            if "?"not in b7 :
                print ("your king may conquer the " ,black_piece(b7)," in b7")
            if "?"not in b8:
                print ("your king may conquer the " ,black_piece(b8)," in b8")
            if "?"not in a8:
                print ("your king may conquer the " ,black_piece(a8)," in a8")
            if "?"not in b6 :
                print ("your king may conquer the " ,black_piece(b6)," in b6")
            if "?"not in a6:
                print ("your king may conquer the ", black_piece(a6)," in a6")
        elif "p" in b7:
            if "?"not in a8 :
                print ("your pawn may conquer the ", black_piece(a8)," in a8")
            if "?"not in c8 :
                print ("your pawn may conquer the ", black_piece(c8)," in c8")
        elif "k" in b7:
            if "?"not in a7 :
                print ("your king may conquer the ", black_piece(a7)," in a7")
            if "?"not in b8:
                print ("your king may conquer the ", black_piece(b8)," in b8")
            if "?"not in a8:
                print ("your king may conquer the ", black_piece(a8)," in a8")
            if "?"not in b6 :
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in a6:
                print ("your king may conquer the ", black_piece(a6)," in a6")
            if "?"not in c6 :
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in c7:
                print ("your king may conquer the ", black_piece(c7)," in c7")
            if "?"not in c8:
                print ("your king may conquer the ", black_piece(c8)," in c8")
        elif "p" in c7:
            if "?"not in b8 :
                print ("your pawn may conquer the ", black_piece(b8)," in b8")
            if "?"not in d8 :
                print ("your pawn may conquer the ", black_piece(d8)," in d8")
        elif "k" in c7:
            if "?"not in b8 :
                print ("your king may conquer the ", black_piece(b8)," in b8")
            if "?"not in c8:
                print ("your king may conquer the ", black_piece(c8)," in c8")
            if "?"not in d8:
                print ("your king may conquer the ", black_piece(d8)," in d8")
            if "?"not in b7 :
                print ("your king may conquer the ", black_piece(b7)," in b7")
            if "?"not in d7:
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in b6 :
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in c6:
                print ("your king may conquer the " ,black_piece(c6)," in c6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
        elif "p" in d7:
            if "?"not in c8 :
                print ("your pawn may conquer the ", black_piece(c8)," in c8")
            if "?"not in e8 :
                print ("your pawn may conquer the ", black_piece(e8)," in e8")
        elif "k" in d7:
            if "?"not in e8 :
                print ("your king may conquer the ", black_piece(e8)," in e8")
            if "?"not in c8:
                print ("your king may conquer the ", black_piece(c8)," in c8")
            if "?"not in d8:
                print ("your king may conquer the ", black_piece(d8)," in d8")
            if "?"not in c7 :
                print ("your king may conquer the ", black_piece(c7)," in c7")
            if "?"not in e7:
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in c6:
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in d6:
                print ("your king may conquer the " ,black_piece(d6)," in d6")
        elif "p" in e7:
            if "?"not in f8 :
                print ("your pawn may conquer the ", black_piece(f8)," in f8")
            if "?"not in d8 :
                print ("your pawn may conquer the ", black_piece(d8)," in d8")
        elif "k" in e7:
            if "?"not in e8 :
                print ("your king may conquer the ", black_piece(e8)," in e8")
            if "?"not in f8:
                print ("your king may conquer the ", black_piece(f8)," in f8")
            if "?"not in d8:
                print ("your king may conquer the ", black_piece(d8)," in d8")
            if "?"not in d7 :
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in f7:
                print ("your king may conquer the ", black_piece(f7)," in f7")
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in f6:
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
        elif "p" in f7:
            if "?"not in e8 :
                print ("your pawn may conquer the ", black_piece(e8)," in e8")
            if "?"not in g8 :
                print ("your pawn may conquer the ", black_piece(g8)," in g8")
        elif "k" in f7:
            if "?"not in e8 :
                print ("your king may conquer the ", black_piece(e8)," in e8")
            if "?"not in f8:
                print ("your king may conquer the ", black_piece(f8)," in f8")
            if "?"not in g8:
                print ("your king may conquer the ", black_piece(g8)," in g8")
            if "?"not in e7 :
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in g7:
                print ("your king may conquer the ", black_piece(g7)," in g7")
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in f6:
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in g6:
                print ("your king may conquer the ", black_piece(g6)," in g6")
        elif "p" in g7:
            if "?"not in f8 :
                print ("your pawn may conquer the " ,black_piece(f8)," in f8")
            if "?"not in h8 :
                print ("your pawn may conquer the ", black_piece(h8)," in h8")
        elif "k" in g7:
            if "?"not in h8 :
                print ("your king may conquer the " ,black_piece(h8)," in h8")
            if "?"not in f8:
                print ("your king may conquer the " ,black_piece(f8)," in f8")
            if "?"not in g8:
                print ("your king may conquer the " ,black_piece(g8)," in g8")
            if "?"not in f7 :
                print ("your king may conquer the ", black_piece(f7)," in f7")
            if "?"not in h7:
                print ("your king may conquer the " ,black_piece(h7)," in h7")
            if "?"not in h6 :
                print ("your king may conquer the ", black_piece(h6)," in h6")
            if "?"not in f6:
                print ("your king may conquer the " ,black_piece(f6)," in f6")
            if "?"not in g6:
                print ("your king may conquer the " ,black_piece(g6)," in g6")
        elif "p" in h7:
            if "?"not in g8 :
                print ("your pawn may conquer the " ,black_piece(g8)," in g8")
        elif "k" in h7:
            if "?"not in h8 :
                print ("your king may conquer the " ,black_piece(h8)," in h8")
            if "?"not in g8:
                print ("your king may conquer the " ,black_piece(g8)," in g8")
            if "?"not in g7 :
                print ("your king may conquer the " ,black_piece(g7)," in g7")
            if "?"not in h6 :
                print ("your king may conquer the " ,black_piece(h6)," in h6")
            if "?"not in g6:
                print ("your king may conquer the " ,black_piece(g6)," in g6")
        elif "p" in a6:
            if "?"not in b7 :
                print ("your pawn may conquer the ", black_piece(b7)," in b7")
        elif "k" in a6:
            if "?"not in b6 :
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in b7:
                print ("your king may conquer the " ,black_piece(b7)," in b7")
            if "?"not in a7:
                print ("your king may conquer the " ,black_piece(a7)," in a7")
            if "?"not in b5 :
                print ("your king may conquer the " ,black_piece(b5)," in b5")
            if "?"not in a5:
                print ("your king may conquer the ", black_piece(a5)," in a5")
        elif "p" in b6:
            if "?"not in a7 :
                print ("your pawn may conquer the ", black_piece(a7)," in a7")
            if "?"not in c7 :
                print ("your pawn may conquer the ", black_piece(c7)," in c7")
        elif "k" in b6:
            if "?"not in a6 :
                print ("your king may conquer the ", black_piece(a6)," in a6")
            if "?"not in b7:
                print ("your king may conquer the ", black_piece(b7)," in b7")
            if "?"not in a7:
                print ("your king may conquer the ", black_piece(a7)," in a7")
            if "?"not in b5 :
                print ("your king may conquer the ", black_piece(b5)," in b5")
            if "?"not in a5:
                print ("your king may conquer the ", black_piece(a5)," in a5")
            if "?"not in c5 :
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in c6:
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in c7:
                print ("your king may conquer the ", black_piece(c7)," in c7")
        elif "p" in c6:
            if "?"not in b7 :
                print ("your pawn may conquer the ", black_piece(b7)," in b7")
            if "?"not in d7 :
                print ("your pawn may conquer the ", black_piece(d7)," in d7")
        elif "k" in c6:
            if "?"not in b7 :
                print ("your king may conquer the ", black_piece(b7)," in b7")
            if "?"not in c7:
                print ("your king may conquer the ", black_piece(c7)," in c7")
            if "?"not in d7:
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in b6 :
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
            if "?"not in b5 :
                print ("your king may conquer the ", black_piece(b5)," in b5")
            if "?"not in c5:
                print ("your king may conquer the " ,black_piece(c5)," in c5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
        elif "p" in d6:
            if "?"not in c7:
                print ("your pawn may conquer the ", black_piece(c7)," in c7")
            if "?"not in e7:
                print ("your pawn may conquer the ", black_piece(e7)," in e7")
        elif "k" in d6:
            if "?"not in e7 :
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in c7:
                print ("your king may conquer the ", black_piece(c7)," in c7")
            if "?"not in d7:
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in c6 :
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in e6:
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in c5:
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in d5:
                print ("your king may conquer the " ,black_piece(d5)," in d5")
        elif "p" in e6:
            if "?"not in f7 :
                print ("your pawn may conquer the ", black_piece(f7)," in f7")
            if "?"not in d7 :
                print ("your pawn may conquer the ", black_piece(d7)," in d7")
        elif "k" in e6:
            if "?"not in e7 :
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in f7:
                print ("your king may conquer the ", black_piece(f7)," in f7")
            if "?"not in d7:
                print ("your king may conquer the ", black_piece(d7)," in d7")
            if "?"not in d6 :
                print ("your king may conquer the ", black_piece(d6)," in d6")
            if "?"not in f6:
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in f5:
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
        elif "p" in f6:
            if "?"not in e7 :
                print ("your pawn may conquer the ", black_piece(e7)," in e7")
            if "?"not in g7 :
                print ("your pawn may conquer the ", black_piece(g7)," in g7")
        elif "k" in f6:
            if "?"not in e7 :
                print ("your king may conquer the ", black_piece(e7)," in e7")
            if "?"not in f7:
                print ("your king may conquer the ", black_piece(f7)," in f7")
            if "?"not in g7:
                print ("your king may conquer the ", black_piece(g7)," in g7")
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in g6:
                print ("your king may conquer the ", black_piece(g6)," in g6")
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in f5:
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in g5:
                print ("your king may conquer the ", black_piece(g5)," in g5")
        elif "p" in g6:
            if "?"not in f7 :
                print ("your pawn may conquer the " ,black_piece(f7)," in f7")
            if "?"not in h7 :
                print ("your pawn may conquer the ", black_piece(h7)," in h7")
        elif "k" in g6:
            if "?"not in h7 :
                print ("your king may conquer the " ,black_piece(h7)," in h7")
            if "?"not in f7:
                print ("your king may conquer the " ,black_piece(f7)," in f7")
            if "?"not in g7:
                print ("your king may conquer the " ,black_piece(g7)," in g7")
            if "?"not in f6 :
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in h6:
                print ("your king may conquer the " ,black_piece(h6)," in h6")
            if "?"not in h5 :
                print ("your king may conquer the ", black_piece(h5)," in h5")
            if "?"not in f5:
                print ("your king may conquer the " ,black_piece(f5)," in f5")
            if "?"not in g5:
                print ("your king may conquer the " ,black_piece(g5)," in g5")
        elif "p" in h6:
            if "?"not in g7 :
                print ("your pawn may conquer the " ,black_piece(g7)," in g7")
        elif "k" in h6:
            if "?"not in h7 :
                print ("your king may conquer the " ,black_piece(h7)," in h7")
            if "?"not in g7:
                print ("your king may conquer the " ,black_piece(g7)," in g7")
            if "?"not in g6 :
                print ("your king may conquer the " ,black_piece(g6)," in g6")
            if "?"not in h5 :
                print ("your king may conquer the " ,black_piece(h5)," in h5")
            if "?"not in g5:
                print ("your king may conquer the " ,black_piece(g5)," in g5")
        elif "p" in a5:
            if "?"not in b6 :
                print ("your pawn may conquer the " ,black_piece(b6)," in b6")
        elif "k" in a5:
            if "?"not in b5 :
                print ("your king may conquer the " ,black_piece(b5)," in b5")
            if "?"not in b6:
                print ("your king may conquer the " ,black_piece(b6)," in b6")
            if "?"not in a6:
                print ("your king may conquer the " ,black_piece(a6)," in a6")
            if "?"not in b4 :
                print ("your king may conquer the " ,black_piece(b4)," in b4")
            if "?"not in a4:
                print ("your king may conquer the " ,black_piece(a4)," in a4")
        elif "p" in b5:
            if "?"not in a6 :
                print ("your pawn may conquer the ", black_piece(a6)," in a6")
            if "?"not in c6 :
                print ("your pawn may conquer the ", black_piece(c6)," in c6")
        elif "k" in b5:
            if "?"not in a5 :
                print ("your king may conquer the ", black_piece(a5)," in a5")
            if "?"not in b6:
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in a6:
                print ("your king may conquer the ", black_piece(a6)," in a6")
            if "?"not in b4 :
                print ("your king may conquer the ", black_piece(b4)," in b4")
            if "?"not in a4:
                print ("your king may conquer the ", black_piece(a4)," in a4")
            if "?"not in c4 :
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in c5:
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in c6:
                print ("your king may conquer the ", black_piece(c6)," in c6")
        elif "p" in c5:
            if "?"not in b6 :
                print ("your pawn may conquer the ", black_piece(b6)," in b6")
            if "?"not in d6 :
                print ("your pawn may conquer the ", black_piece(d6)," in d6")
        elif "k" in c5:
            if "?"not in b6 :
                print ("your king may conquer the ", black_piece(b6)," in b6")
            if "?"not in c6:
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
            if "?"not in b5 :
                print ("your king may conquer the ", black_piece(b5)," in b5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
            if "?"not in b4 :
                print ("your king may conquer the ", black_piece(b4)," in b4")
            if "?"not in c4:
                print ("your king may conquer the " ,black_piece(c4)," in c4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
        elif "p" in d5:
            if "?"not in c6 :
                print ("your pawn may conquer the ", black_piece(c6)," in c6")
            if "?"not in e6 :
                print ("your pawn may conquer the ", black_piece(e6)," in e6")
        elif "k" in d5:
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in c6:
                print ("your king may conquer the ", black_piece(c6)," in c6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
            if "?"not in c5 :
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in e5:
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in c4:
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in d4:
                print ("your king may conquer the " ,black_piece(d4)," in d4")
        elif "p" in e5:
            if "?"not in f6 :
                print ("your pawn may conquer the ", black_piece(f6)," in f6")
            if "?"not in d6 :
                print ("your pawn may conquer the ", black_piece(d6)," in d6")
        elif "k" in e5:
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in f6:
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in d6:
                print ("your king may conquer the ", black_piece(d6)," in d6")
            if "?"not in d5 :
                print ("your king may conquer the ", black_piece(d5)," in d5")
            if "?"not in f5:
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in f4:
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
        elif "p" in f5:
            if "?"not in e6 :
                print ("your pawn may conquer the ", black_piece(e6)," in e6")
            if "?"not in g6 :
                print ("your pawn may conquer the ", black_piece(g6)," in g6")
        elif "k" in f5:
            if "?"not in e6 :
                print ("your king may conquer the ", black_piece(e6)," in e6")
            if "?"not in f6:
                print ("your king may conquer the ", black_piece(f6)," in f6")
            if "?"not in g6:
                print ("your king may conquer the ", black_piece(g6)," in g6")
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in g5:
                print ("your king may conquer the ", black_piece(g5)," in g5")
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in f4:
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in g4:
                print ("your king may conquer the ", black_piece(g4)," in g4")
        elif "p" in g5:
            if "?"not in f6 :
                print ("your pawn may conquer the " ,black_piece(f6)," in f6")
            if "?"not in h6 :
                print ("your pawn may conquer the ", black_piece(h6)," in h6")
        elif "k" in g5:
            if "?"not in h6 :
                print ("your king may conquer the " ,black_piece(h6)," in h6")
            if "?"not in f6:
                print ("your king may conquer the " ,black_piece(f6)," in f6")
            if "?"not in g6:
                print ("your king may conquer the " ,black_piece(g6)," in g6")
            if "?"not in f5 :
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in h5:
                print ("your king may conquer the " ,black_piece(h5)," in h5")
            if "?"not in h4 :
                print ("your king may conquer the ", black_piece(h4)," in h4")
            if "?"not in f4:
                print ("your king may conquer the " ,black_piece(f4)," in f4")
            if "?"not in g4:
                print ("your king may conquer the " ,black_piece(g4)," in g4")
        elif "p" in h5:
            if "?"not in g6 :
                print ("your pawn may conquer the " ,black_piece(g6)," in g6")
        elif "k" in h5:
            if "?"not in h6 :
                print ("your king may conquer the " ,black_piece(h6)," in h6")
            if "?"not in g6:
                print ("your king may conquer the " ,black_piece(g6)," in g6")
            if "?"not in g5 :
                print ("your king may conquer the " ,black_piece(g5)," in g5")
            if "?"not in h4 :
                print ("your king may conquer the " ,black_piece(h4)," in h4")
            if "?"not in g4:
                print ("your king may conquer the " ,black_piece(g4)," in g4")
        elif "p" in a4:
            if "?"not in b5 :
                print ("your pawn may conquer the " ,black_piece(b5)," in b5")
        elif "k" in a4:
            if "?"not in b4 :
                print ("your king may conquer the " ,black_piece(b4)," in b4")
            if "?"not in b5:
                print ("your king may conquer the " ,black_piece(b5)," in b5")
            if "?"not in a5:
                print ("your king may conquer the " ,black_piece(a5)," in a5")
            if "?"not in b3 :
                print ("your king may conquer the " ,black_piece(b3)," in b3")
            if "?"not in a3:
                print ("your king may conquer the " ,black_piece(a3)," in a3")
        elif "p" in b4:
            if "?"not in a5 :
                print ("your pawn may conquer the ", black_piece(a5)," in a5")
            if "?"not in c5 :
                print ("your pawn may conquer the ", black_piece(c5)," in c5")
        elif "k" in b4:
            if "?"not in a4 :
                print ("your king may conquer the ", black_piece(a4)," in a4")
            if "?"not in b5:
                print ("your king may conquer the ", black_piece(b5)," in b5")
            if "?"not in a5:
                print ("your king may conquer the ", black_piece(a5)," in a5")
            if "?"not in b3 :
                print ("your king may conquer the ", black_piece(b3)," in b3")
            if "?"not in a3:
                print ("your king may conquer the ", black_piece(a3)," in a3")
            if "?"not in c3 :
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in c4:
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in c5:
                print ("your king may conquer the ", black_piece(c5)," in c5")
        elif "p" in c4:
            if "?"not in b5 :
                print ("your pawn may conquer the ", black_piece(b5)," in b5")
            if "?"not in d5 :
                print ("your pawn may conquer the ", black_piece(d5)," in d5")
        elif "k" in c4:
            if "?"not in b5 :
                print ("your king may conquer the ", black_piece(b5)," in b5")
            if "?"not in c5:
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
            if "?"not in b4 :
                print ("your king may conquer the ", black_piece(b4)," in b4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
            if "?"not in b3 :
                print ("your king may conquer the ", black_piece(b3)," in b3")
            if "?"not in c3:
                print ("your king may conquer the " ,black_piece(c3)," in c3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
        elif "p" in d4:
            if "?"not in c5 :
                print ("your pawn may conquer the ", black_piece(c5)," in c5")
            if "?"not in e5 :
                print ("your pawn may conquer the ", black_piece(e5)," in e5")
        elif "k" in d4:
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in c5:
                print ("your king may conquer the ", black_piece(c5)," in c5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
            if "?"not in c4 :
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in e4:
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in c3:
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in d3:
                print ("your king may conquer the " ,black_piece(d3)," in d3")
        elif "p" in e4:
            if "?"not in f5 :
                print ("your pawn may conquer the ", black_piece(f5)," in f5")
            if "?"not in d5 :
                print ("your pawn may conquer the ", black_piece(d5)," in d5")
        elif "k" in e4:
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in f5:
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in d5:
                print ("your king may conquer the ", black_piece(d5)," in d5")
            if "?"not in d4 :
                print ("your king may conquer the ", black_piece(d4)," in d4")
            if "?"not in f4:
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in f3:
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
        elif "p" in f4:
            if "?"not in e5 :
                print ("your pawn may conquer the ", black_piece(e5)," in e5")
            if "?"not in g5 :
                print ("your pawn may conquer the ", black_piece(g5)," in g5")
        elif "k" in f4:
            if "?"not in e5 :
                print ("your king may conquer the ", black_piece(e5)," in e5")
            if "?"not in f5:
                print ("your king may conquer the ", black_piece(f5)," in f5")
            if "?"not in g5:
                print ("your king may conquer the ", black_piece(g5)," in g5")
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in g4:
                print ("your king may conquer the ", black_piece(g4)," in g4")
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in f3:
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in g3:
                print ("your king may conquer the ", black_piece(g3)," in g3")
        elif "p" in g4:
            if "?"not in f5 :
                print ("your pawn may conquer the " ,black_piece(f5)," in f5")
            if "?"not in h5 :
                print ("your pawn may conquer the ", black_piece(h5)," in h5")
        elif "k" in g4:
            if "?"not in h5 :
                print ("your king may conquer the " ,black_piece(h5)," in h5")
            if "?"not in f5:
                print ("your king may conquer the " ,black_piece(f5)," in f5")
            if "?"not in g5:
                print ("your king may conquer the " ,black_piece(g5)," in g5")
            if "?"not in f4 :
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in h4:
                print ("your king may conquer the " ,black_piece(h4)," in h4")
            if "?"not in h3 :
                print ("your king may conquer the ", black_piece(h3)," in h3")
            if "?"not in f3:
                print ("your king may conquer the " ,black_piece(f3)," in f3")
            if "?"not in g3:
                print ("your king may conquer the " ,black_piece(g3)," in g3")
        elif "p" in h4:
            if "?"not in g5 :
                print ("your pawn may conquer the " ,black_piece(g5)," in g5")
        elif "k" in h4:
            if "?"not in h5 :
                print ("your king may conquer the " ,black_piece(h5)," in h5")
            if "?"not in g5:
                print ("your king may conquer the " ,black_piece(g5)," in g5")
            if "?"not in g4 :
                print ("your king may conquer the " ,black_piece(g4)," in g4")
            if "?"not in h3 :
                print ("your king may conquer the " ,black_piece(h3)," in h3")
            if "?"not in g3:
                print ("your king may conquer the " ,black_piece(g3)," in g3")
        elif "p" in a3:
            if "?"not in b4 :
                print ("your pawn may conquer the " ,black_piece(b4)," in b4")
        elif "k" in a3:
            if "?"not in b3 :
                print ("your king may conquer the " ,black_piece(b3)," in b3")
            if "?"not in b4:
                print ("your king may conquer the " ,black_piece(b4)," in b4")
            if "?"not in a4:
                print ("your king may conquer the " ,black_piece(a4)," in a4")
            if "?"not in b2 :
                print ("your king may conquer the " ,black_piece(b2)," in b2")
            if "?"not in a2:
                print ("your king may conquer the " ,black_piece(a2)," in a2")
        elif "p" in b3:
            if "?"not in a4 :
                print ("your pawn may conquer the ", black_piece(a4)," in a4")
            if "?"not in c4 :
                print ("your pawn may conquer the ", black_piece(c4)," in c4")
        elif "k" in b3:
            if "?"not in a3 :
                print ("your king may conquer the ", black_piece(a3)," in a3")
            if "?"not in b4:
                print ("your king may conquer the ", black_piece(b4)," in b4")
            if "?"not in a4:
                print ("your king may conquer the ", black_piece(a4)," in a4")
            if "?"not in b2 :
                print ("your king may conquer the ", black_piece(b2)," in b2")
            if "?"not in a2:
                print ("your king may conquer the ", black_piece(a2)," in a2")
            if "?"not in c2 :
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in c3:
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in c4:
                print ("your king may conquer the ", black_piece(c4)," in c4")
        elif "p" in c3:
            if "?"not in b4 :
                print ("your pawn may conquer the ", black_piece(b4)," in b4")
            if "?"not in d4 :
                print ("your pawn may conquer the ", black_piece(d4)," in d4")
        elif "k" in c3:
            if "?"not in b4 :
                print ("your king may conquer the ", black_piece(b4)," in b4")
            if "?"not in c4:
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
            if "?"not in b3 :
                print ("your king may conquer the ", black_piece(b3)," in b3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
            if "?"not in b2 :
                print ("your king may conquer the ", black_piece(b2)," in b2")
            if "?"not in c2:
                print ("your king may conquer the " ,black_piece(c2)," in c2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
        elif "p" in d3:
            if "?"not in c4 :
                print ("your pawn may conquer the ", black_piece(c4)," in c4")
            if "?"not in e4 :
                print ("your pawn may conquer the ", black_piece(e4)," in e4")
        elif "k" in d3:
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in c4:
                print ("your king may conquer the ", black_piece(c4)," in c4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
            if "?"not in c3 :
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in e3:
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in c2:
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in d2:
                print ("your king may conquer the " ,black_piece(d2)," in d2")
        elif "p" in e3:
            if "?"not in f4 :
                print ("your pawn may conquer the ", black_piece(f4)," in f4")
            if "?"not in d4 :
                print ("your pawn may conquer the ", black_piece(d4)," in d4")
        elif "k" in e3:
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in f4:
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in d4:
                print ("your king may conquer the ", black_piece(d4)," in d4")
            if "?"not in d3 :
                print ("your king may conquer the ", black_piece(d3)," in d3")
            if "?"not in f3:
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in f2:
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
        elif "p" in f3:
            if "?"not in e4 :
                print ("your pawn may conquer the ", black_piece(e4)," in e4")
            if "?"not in g4 :
                print ("your pawn may conquer the ", black_piece(g4)," in g4")
        elif "k" in f3:
            if "?"not in e4 :
                print ("your king may conquer the ", black_piece(e4)," in e4")
            if "?"not in f4:
                print ("your king may conquer the ", black_piece(f4)," in f4")
            if "?"not in g4:
                print ("your king may conquer the ", black_piece(g4)," in g4")
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in g3:
                print ("your king may conquer the ", black_piece(g3)," in g3")
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in f2:
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in g2:
                print ("your king may conquer the ", black_piece(g2)," in g2")
        elif "p" in g3:
            if "?"not in f4 :
                print ("your pawn may conquer the " ,black_piece(f4)," in f4")
            if "?"not in h4 :
                print ("your pawn may conquer the ", black_piece(h4)," in h4")
        elif "k" in g3:
            if "?"not in h4 :
                print ("your king may conquer the " ,black_piece(h4)," in h4")
            if "?"not in f4:
                print ("your king may conquer the " ,black_piece(f4)," in f4")
            if "?"not in g4:
                print ("your king may conquer the " ,black_piece(g4)," in g4")
            if "?"not in f3 :
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in h3:
                print ("your king may conquer the " ,black_piece(h3)," in h3")
            if "?"not in h2 :
                print ("your king may conquer the ", black_piece(h2)," in h2")
            if "?"not in f2:
                print ("your king may conquer the " ,black_piece(f2)," in f2")
            if "?"not in g2:
                print ("your king may conquer the " ,black_piece(g2)," in g2")
        elif "p" in h3:
            if "?"not in g4 :
                print ("your pawn may conquer the " ,black_piece(g4)," in g4")
        elif "k" in h3:
            if "?"not in h4 :
                print ("your king may conquer the " ,black_piece(h4)," in h4")
            if "?"not in g4:
                print ("your king may conquer the " ,black_piece(g4)," in g4")
            if "?"not in g3 :
                print ("your king may conquer the " ,black_piece(g3)," in g3")
            if "?"not in h2 :
                print ("your king may conquer the " ,black_piece(h2)," in h2")
            if "?"not in g2:
                print ("your king may conquer the " ,black_piece(g2)," in g2")
        elif "p" in a2:
            if "?"not in b3 :
                print ("your pawn may conquer the " ,black_piece(b3)," in b3")
        elif "k" in a2:
            if "?"not in b2 :
                print ("your king may conquer the " ,black_piece(b2)," in b2")
            if "?"not in b3:
                print ("your king may conquer the " ,black_piece(b3)," in b3")
            if "?"not in a3:
                print ("your king may conquer the " ,black_piece(a3)," in a3")
            if "?"not in b1 :
                print ("your king may conquer the " ,black_piece(b1)," in b1")
            if "?"not in a1:
                print ("your king may conquer the " ,black_piece(a1)," in a1")
        elif "p" in b2:
            if "?"not in a3 :
                print ("your pawn may conquer the ", black_piece(a3)," in a3")
            if "?"not in c3 :
                print ("your pawn may conquer the ", black_piece(c3)," in c3")
        elif "k" in b2:
            if "?"not in a2 :
                print ("your king may conquer the ", black_piece(a2)," in a2")
            if "?"not in b3:
                print ("your king may conquer the ", black_piece(b3)," in b3")
            if "?"not in a3:
                print ("your king may conquer the ", black_piece(a3)," in a3")
            if "?"not in b1 :
                print ("your king may conquer the ", black_piece(b1)," in b1")
            if "?"not in a1:
                print ("your king may conquer the ", black_piece(a1)," in a1")
            if "?"not in c1 :
                print ("your king may conquer the ", black_piece(c1)," in c1")
            if "?"not in c2:
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in c3:
                print ("your king may conquer the ", black_piece(c3)," in c3")
        elif "p" in c2:
            if "?"not in b3 :
                print ("your pawn may conquer the ", black_piece(b3)," in b3")
            if "?"not in d3 :
                print ("your pawn may conquer the ", black_piece(d3)," in d3")
        elif "k" in c2:
            if "?"not in b3 :
                print ("your king may conquer the ", black_piece(b3)," in b3")
            if "?"not in c3:
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
            if "?"not in b2 :
                print ("your king may conquer the ", black_piece(b2)," in b2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
            if "?"not in b1 :
                print ("your king may conquer the ", black_piece(b1)," in b1")
            if "?"not in c1:
                print ("your king may conquer the " ,black_piece(c1)," in c1")
            if "?"not in d1:
                print ("your king may conquer the ", black_piece(d1)," in d1")
        elif "p" in d2:
            if "?"not in c3 :
                print ("your pawn may conquer the ", black_piece(c3)," in c3")
            if "?"not in e3 :
                print ("your pawn may conquer the ", black_piece(e3)," in e3")
        elif "k" in d2:
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in c3:
                print ("your king may conquer the ", black_piece(c3)," in c3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
            if "?"not in c2 :
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in e2:
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in e1 :
                print ("your king may conquer the ", black_piece(e1)," in e1")
            if "?"not in c1:
                print ("your king may conquer the ", black_piece(c1)," in c1")
            if "?"not in d1:
                print ("your king may conquer the " ,black_piece(d1)," in d1")
        elif "p" in e2:
            if "?"not in f3 :
                print ("your pawn may conquer the ", black_piece(f3)," in f3")
            if "?"not in d3 :
                print ("your pawn may conquer the ", black_piece(d3)," in d3")
        elif "k" in e2:
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in f3:
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in d3:
                print ("your king may conquer the ", black_piece(d3)," in d3")
            if "?"not in d2 :
                print ("your king may conquer the ", black_piece(d2)," in d2")
            if "?"not in f2:
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in e1 :
                print ("your king may conquer the ", black_piece(e1)," in e1")
            if "?"not in f1:
                print ("your king may conquer the ", black_piece(f1)," in f1")
            if "?"not in d1:
                print ("your king may conquer the ", black_piece(d1)," in d1")
        elif "p" in f2:
            if "?"not in e3 :
                print ("your pawn may conquer the ", black_piece(e3)," in e3")
            if "?"not in g3 :
                print ("your pawn may conquer the ", black_piece(g3)," in g3")
        elif "k" in f2:
            if "?"not in e3 :
                print ("your king may conquer the ", black_piece(e3)," in e3")
            if "?"not in f3:
                print ("your king may conquer the ", black_piece(f3)," in f3")
            if "?"not in g3:
                print ("your king may conquer the ", black_piece(g3)," in g3")
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in g2:
                print ("your king may conquer the ", black_piece(g2)," in g2")
            if "?"not in e1 :
                print ("your king may conquer the ", black_piece(e1)," in e1")
            if "?"not in f1:
                print ("your king may conquer the ", black_piece(f1)," in f1")
            if "?"not in g1:
                print ("your king may conquer the ", black_piece(g1)," in g1")
        elif "p" in g2:
            if "?"not in f3 :
                print ("your pawn may conquer the " ,black_piece(f3)," in f3")
            if "?"not in h3 :
                print ("your pawn may conquer the ", black_piece(h3)," in h3")
        elif "k" in g2:
            if "?"not in h3 :
                print ("your king may conquer the " ,black_piece(h3)," in h3")
            if "?"not in f3:
                print ("your king may conquer the " ,black_piece(f3)," in f3")
            if "?"not in g3:
                print ("your king may conquer the " ,black_piece(g3)," in g3")
            if "?"not in f2 :
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in h2:
                print ("your king may conquer the " ,black_piece(h2)," in h2")
            if "?"not in h1 :
                print ("your king may conquer the ", black_piece(h1)," in h1")
            if "?"not in f1:
                print ("your king may conquer the " ,black_piece(f1)," in f1")
            if "?"not in g1:
                print ("your king may conquer the " ,black_piece(g1)," in g1")
        elif "p" in h2:
            if "?"not in g3 :
                print ("your pawn may conquer the " ,black_piece(g3)," in g3")
        elif "k" in h2:
            if "?"not in h3 :
                print ("your king may conquer the " ,black_piece(h3)," in h3")
            if "?"not in g3:
                print ("your king may conquer the " ,black_piece(g3)," in g3")
            if "?"not in g2 :
                print ("your king may conquer the " ,black_piece(g2)," in g2")
            if "?"not in h1 :
                print ("your king may conquer the " ,black_piece(h1)," in h1")
            if "?"not in g1:
                print ("your king may conquer the " ,black_piece(g1)," in g1")
        elif "p" in a1 or "p" in b1 or "p" in c1 or "p" in d1 or "p" in f1 or "p" in g1 or "p"in h1:
            print ("your pawn cannot be here")
        elif "k" in a1:
            if "?"not in b2:
                print ("your king may conquer the " ,black_piece(b2)," in b2")
            if "?"not in a2:
                print ("your king may conquer the " ,black_piece(a2)," in a2")
            if "?"not in b1 :
                print ("your king may conquer the " ,black_piece(b1)," in b1")
        elif "k" in b1:
            if "?"not in a2 :
                print ("your king may conquer the ", black_piece(a2)," in a2")
            if "?"not in b2:
                print ("your king may conquer the ", black_piece(b2)," in b2")
            if "?"not in c2:
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in c1 :
                print ("your king may conquer the ", black_piece(c1)," in c1")
            if "?"not in a1:
                print ("your king may conquer the ", black_piece(a1)," in a1")
        elif "k" in c1:
            if "?"not in b2 :
                print ("your king may conquer the ", black_piece(b2)," in b2")
            if "?"not in c2:
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
            if "?"not in b1 :
                print ("your king may conquer the ", black_piece(b1)," in b1")
            if "?"not in d1:
                print ("your king may conquer the ", black_piece(d1)," in d1")
        elif "k" in d1:
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in c2:
                print ("your king may conquer the ", black_piece(c2)," in c2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
            if "?"not in c1 :
                print ("your king may conquer the ", black_piece(c1)," in c1")
            if "?"not in e1:
                print ("your king may conquer the ", black_piece(e1)," in e1")
        elif "k" in e1:
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in f2:
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in d2:
                print ("your king may conquer the ", black_piece(d2)," in d2")
            if "?"not in d1 :
                print ("your king may conquer the ", black_piece(d1)," in d1")
            if "?"not in f1:
                print ("your king may conquer the ", black_piece(f1)," in f1")
        elif "k" in f1:
            if "?"not in e2 :
                print ("your king may conquer the ", black_piece(e2)," in e2")
            if "?"not in f2:
                print ("your king may conquer the ", black_piece(f2)," in f2")
            if "?"not in g2:
                print ("your king may conquer the ", black_piece(g2)," in g2")
            if "?"not in e1 :
                print ("your king may conquer the ", black_piece(e1)," in e1")
            if "?"not in g1:
                print ("your king may conquer the ", black_piece(g1)," in g1")
        elif "k" in g1:
            if "?"not in h2 :
                print ("your king may conquer the " ,black_piece(h2)," in h2")
            if "?"not in f2:
                print ("your king may conquer the " ,black_piece(f2)," in f2")
            if "?"not in g2:
                print ("your king may conquer the " ,black_piece(g2)," in g2")
            if "?"not in f1 :
                print ("your king may conquer the ", black_piece(f1)," in f1")
            if "?"not in h1:
                print ("your king may conquer the " ,black_piece(h1)," in h1")
        elif "k" in h1:
            if "?"not in h2 :
                print ("your king may conquer the " ,black_piece(h2)," in h2")
            if "?"not in g2:
                print ("your king may conquer the " ,black_piece(g2)," in g2")
            if "?"not in g1 :
                print ("your king may conquer the " ,black_piece(g1)," in g1")


    #define what piece would be in the players board
def white(x):
    if x == "king":
        return "k"
    elif x== "pawn":
        return "p"
    else:
        print("Piece not found")
#define what pieces in the enemy board
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
#give back the name of the piece to conquer
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

"""
what pieces are in the black side?
any preference of what 2 pieces to program on the white side?
since we are always playing on the white side the pieces can only move in one diretion

"""