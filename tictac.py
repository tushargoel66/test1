import os
import random


board=[" "," "," "," "," "," "," "," "," "]


def checkBullEye():
    if (board[0]=="O" and board[1]=="O" and board[2]==" ")or(board[2]==" " and board[5]=="O" and board[8]=="O")or(board[2]==" " and board[4]=="O" and board[6]=="O"):
        return 2
    if (board[0]==" " and board[1]=="O" and board[2]=="O")or(board[0]==" " and board[4]=="O" and board[8]=="O")or(board[0]==" " and board[3]=="O" and board[6]=="O"):
        return 0
    if (board[0]=="O" and board[1]==" " and board[2]=="O")or(board[1]==" " and board[4]=="O" and board[7]=="O"):
        return 1
    if (board[3]=="O" and board[4]=="O" and board[5]==" ")or(board[2]=="O" and board[5]==" " and board[8]=="O"):
        return 5
    if (board[3]==" " and board[4]=="O" and board[5]=="O")or(board[0]=="O" and board[3]==" " and board[6]=="O"):
        return 3
    if (board[3]=="O" and board[4]==" " and board[5]=="O")or(board[0]=="O" and board[4]==" " and board[8]=="O")or(board[2]=="O" and board[4]==" " and board[6]=="O")or(board[1]=="O" and board[4]==" " and board[7]=="O"):
        return 4
    if (board[6]=="O" and board[7]=="O" and board[8]==" ") or (board[0]=="O" and board[4]=="O" and board[8]==" ")or(board[2]=="O" and board[5]=="O" and board[8]==" "):
        return 8
    if (board[6]==" " and board[7]=="O" and board[8]=="O")or(board[2]=="O" and board[4]=="O" and board[6]==" ")or(board[0]=="O" and board[3]=="O" and board[6]==" "):
        return 6
    if (board[6]=="O" and board[7]==" " and board[8]=="O")or(board[1]=="O" and board[4]=="O" and board[7]==" "):
        return 7
    return -1

def checkPlayer():
    if (board[0]=="X" and board[1]=="X" and board[2]==" ")or(board[2]==" " and board[5]=="X" and board[8]=="X")or(board[2]==" " and board[4]=="X" and board[6]=="X"):
        return 2
    if (board[0]==" " and board[1]=="X" and board[2]=="X")or(board[0]==" " and board[4]=="X" and board[8]=="X")or(board[0]==" " and board[3]=="X" and board[6]=="X"):
        return 0
    if (board[0]=="X" and board[1]==" " and board[2]=="X")or(board[1]==" " and board[4]=="X" and board[7]=="X"):
        return 1
    if (board[3]=="X" and board[4]=="X" and board[5]==" ")or(board[2]=="X" and board[5]==" " and board[8]=="X"):
        return 5
    if (board[3]==" " and board[4]=="X" and board[5]=="X")or(board[0]=="X" and board[3]==" " and board[6]=="X"):
        return 3
    if (board[3]=="X" and board[4]==" " and board[5]=="X")or(board[0]=="X" and board[4]==" " and board[8]=="X")or(board[2]=="X" and board[4]==" " and board[6]=="X")or(board[1]=="X" and board[4]==" " and board[7]=="X"):
        return 4
    if (board[6]=="X" and board[7]=="X" and board[8]==" ") or (board[0]=="X" and board[4]=="X" and board[8]==" ")or(board[2]=="X" and board[5]=="X" and board[8]==" "):
        return 8
    if (board[6]==" " and board[7]=="X" and board[8]=="X")or(board[2]=="X" and board[4]=="X" and board[6]==" ")or(board[0]=="X" and board[3]=="X" and board[6]==" "):
        return 6
    if (board[6]=="X" and board[7]==" " and board[8]=="X")or(board[1]=="X" and board[4]=="X" and board[7]==" "):
        return 7
    return -1


   

def checkComputerWin():
    if(board[0]=="O" and board[1]=="O" and board[2]=="O"):
        return True
    elif(board[3]=="O" and board[4]=="O" and board[5]=="O"):
        return True
    elif(board[6]=="O" and board[7]=="O" and board[8]=="O"):
        return True
    elif(board[0]=="O" and board[4]=="O" and board[8]=="O"):
        return True
    elif(board[2]=="O" and board[4]=="O" and board[6]=="O"):
        return True
    elif(board[0]=="O" and board[3]=="O" and board[6]=="O"):
        return True
    elif(board[1]=="O" and board[4]=="O" and board[7]=="O"):
        return True
    elif(board[2]=="O" and board[5]=="O" and board[8]=="O"):
        return True
    return False

def checkPlayerWin():
    if(board[0]=="X" and board[1]=="X" and board[2]=="X"):
        return True
    elif(board[3]=="X" and board[4]=="X" and board[5]=="X"):
        return True
    elif(board[6]=="X" and board[7]=="X" and board[8]=="X"):
        return True
    elif(board[0]=="X" and board[4]=="X" and board[8]=="X"):
        return True
    elif(board[2]=="X" and board[4]=="X" and board[6]=="X"):
        return True
    elif(board[0]=="X" and board[3]=="X" and board[6]=="X"):
        return True
    elif(board[1]=="X" and board[4]=="X" and board[7]=="X"):
        return True
    elif(board[2]=="X" and board[5]=="X" and board[8]=="X"):
        return True
    return False

def getMove():
    for i in range(0,9):
        if board[i]==" ":
            comp=checkBullEye()
            if comp>0:
                board[comp]="O"
                return
            play=checkPlayer()
            if play>0:
                board[play]="O"
                return
            
    
    if board[4] ==" ":
        board[4]="O"
    else:
        while True:
            slot=random.randint(0,8)
            if board[slot]==" ":
                board[slot]="O"
                break

def checkTie():
    for i in range(0,9):
        if board[i]==" ":
            return False
    return True



def display_board():
    """Display game board on screen."""
    print()
    print("   "+board[0] + " | " +board[1] + " | " + board[2]) 
    print()
    print("   "+board[3] + " | " +board[4] + " | " + board[5]) 
    print()
    print("   "+board[6] + " | " +board[7] + " | " + board[8])
    print()



_ = os.system('cls')
f=False
p=True
while True:
    if f==False:
        choice=input("Are you making the first move (y/n)?")
    else:
        choice=input("Please enter (y/n)")
    if choice == "y" or choice =="n":
        break
    else:
        f=True
print("Your moves are Xs")

if choice=="y":
    while True:
        display_board()    
        play=raw_input("Enter your move : ")
        if play.isdigit():
            player=int(play)
            err=False
            if player>9:
                print("Enter numbers between 0-8")
                err=True
            else:
                if err==False:
                    if board[player]==" ":  
                        board[player]="X"
                        display_board() 
                        if checkTie():
                            display_board()
                            print("Match Tied")
                            break
                        if checkPlayerWin():
                            display_board()
                            print("You won!!")
                            break
                    else:
                        err=True
                        print("Slot already covered")
            if err==False: 
                print("Computer Move : \n")    
                comp=getMove()
                if checkTie():
                    display_board()
                    print("Match Tied")
                    break
                if checkComputerWin():
                    display_board()
                    print("Computer Won")
                    break
        else:
            print("Only integer allowed")
else:
    while True:
        err=False
        if p==True:
            if err==False:
                print("\nComputer Move : \n")         
                comp=getMove()
                if checkTie():
                    display_board() 
                    print("Match Tied")
                    break
                if checkComputerWin():
                    display_board() 
                    print("Computer Won")
                    break 

        display_board() 
        play=raw_input("Enter your move : ")
        if play.isdigit():
            player=int(play)
            if player>9:
                print("Enter numbers between 0-8")
                err=True
                p=False
            else:
                if err==False:
                    if board[player]==" ":  
                        board[player]="X"
                        p=True
                        if checkTie():
                            display_board() 
                            print("Match Tied")
                            break
                        if checkPlayerWin():
                            display_board() 
                            print("You won!!")
                            break
                    else:
                        err=True
                        p=False
                        print("Slot already covered")
        else:
            p=False
            print("Only integer allowed")
                    
        
