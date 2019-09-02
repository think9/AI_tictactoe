import pickle
from tkinter import *
from tkinter import messagebox
import numpy as np

with open("W_param.pkl", 'rb') as f:
    W = pickle.load(f)

with open("W2_param.pkl", 'rb') as f:
    W2 = pickle.load(f)

with open("B_param.pkl", 'rb') as f:
    B = pickle.load(f)

with open("B2_param.pkl", 'rb') as f:
    B2 = pickle.load(f)

def forward(X):
    hidden = np.matmul(X, W) + B
    hidden = 1 / (1 + np.exp(-hidden))
    result = np.matmul(hidden, W2) + B2
    return result

def findBlank(myBoard):
    print(myBoard)
    predict = -100
    index = 0
    board = myBoard
    for i in range(len(board)):
        if(board[i]==0):
            board[i] = 1
            result = forward(board)
            print(i, result)
            #컴퓨터가 먼저 시 최솟값
            #사람이 먼저 시 최댓값
            if(predict < result):
                predict = result
                index = i
            board[i]=0
    print("computer : " + str(index) + ", " + str(predict))
    return index

#Game

window=Tk()

window.title("AI Tic-Tac-Toe")
window.geometry("400x300")

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn=1; #For first person turn.

global board
global next
global first
next = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
first = 1

def put(next):
    if next==0:
        clicked1()
    elif next==1:
        clicked2()
    elif next==2:
        clicked3()
    elif next==3:
        clicked4()
    elif next==4:
        clicked5()
    elif next==5:
        clicked6()
    elif next==6:
        clicked7()
    elif next==7:
        clicked8()
    elif next==8:
        clicked9()

def clicked1():
    global turn
    global next
    global first
    if btn1["text"]==" ":   #For getting the text of a button
        if turn==1:
            turn =2;
            board[0] = -1
            btn1["text"]="X"
        elif turn==2:
            turn=1;
            board[0] = 1
            btn1["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked2():
    global turn
    global next
    global first
    if btn2["text"]==" ":
        if turn==1:
            turn =2;
            board[1] = -1
            btn2["text"]="X"
        elif turn==2:
            turn=1;
            board[1] = 1
            btn2["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked3():
    global turn
    global next
    global first
    if btn3["text"]==" ":
        if turn==1:
            turn =2;
            board[2] = -1
            btn3["text"]="X"
        elif turn==2:
            turn=1;
            board[2] = 1
            btn3["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked4():
    global turn
    global next
    global first
    if btn4["text"]==" ":
        if turn==1:
            turn =2;
            board[3] = -1
            btn4["text"]="X"
        elif turn==2:
            turn=1;
            board[3] = 1
            btn4["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked5():
    global turn
    global next
    global first
    if btn5["text"]==" ":
        if turn==1:
            turn =2;
            board[4] = -1
            btn5["text"]="X"
        elif turn==2:
            turn=1;
            board[4] = 1
            btn5["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked6():
    global turn
    global next
    global first
    if btn6["text"]==" ":
        if turn==1:
            turn =2;
            board[5] = -1
            btn6["text"]="X"
        elif turn==2:
            turn=1;
            board[5] = 1
            btn6["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked7():
    global turn
    global next
    global first
    if btn7["text"]==" ":
        if turn==1:
            turn =2;
            board[6] = -1
            btn7["text"]="X"
        elif turn==2:
            turn=1;
            board[6] = 1
            btn7["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked8():
    global turn
    global next
    global first
    if btn8["text"]==" ":
        if turn==1:
            turn =2;
            board[7] = -1
            btn8["text"]="X"
        elif turn==2:
            turn=1;
            board[7] = 1
            btn8["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

def clicked9():
    global turn
    global next
    global first
    if btn9["text"]==" ":
        if turn==1:
            turn =2;
            board[8] = -1
            btn9["text"]="X"
        elif turn==2:
            turn=1;
            board[8] = 1
            btn9["text"]="O"
        check();
        if turn==first:
            put(findBlank(board))

flag=1;
def check():
    global flag;
    b1 = btn1["text"];
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag=flag+1;
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"]);
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"]);
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"]);
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"]);
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"]);
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"]);
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"]);
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
btn9.grid(column=3, row=3)

window.mainloop()