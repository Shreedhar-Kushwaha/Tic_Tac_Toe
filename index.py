from tkinter import *
root = Tk()
root.title("Shreedhar")

def callback(r,c):
    global player
    if player=='X' and states[r][c]==0 and stop_game==False:
        m[r][c].configure(text="X",fg='blue',bg='white')
        states[r][c]='X'
        player='O'
    if player=='O' and states[r][c]==0 and stop_game==False:
        m[r][c].configure(text="O",fg='orange',bg='black')
        states[r][c]='O'
        player='X'
    check_for_winner()
def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            m[i][0].configure(bg='grey')
            m[i][1].configure(bg='grey')
            m[i][2].configure(bg='grey')
            stop_game=True
    for j in range(3):
        if states[0][j]==states[1][j]==states[2][j]!=0:
            m[0][j].configure(bg='grey')
            m[1][j].configure(bg='grey')
            m[2][j].configure(bg='grey')
            stop_game=True
    if states[0][0]==states[1][1]==states[2][2]!=0:
        m[0][0].configure(bg='grey')
        m[1][1].configure(bg='grey')
        m[2][2].configure(bg='grey')
        stop_game = True
    if states[0][2]==states[1][1]==states[2][0]!=0:
        m[0][2].configure(bg='grey')
        m[1][1].configure(bg='grey')
        m[2][0].configure(bg='grey')
        stop_game = True

m=[[0,0,0],
   [0,0,0],
   [0,0,0]]
states=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(3):

    for j in range(3):
        m[i][j]=Button(font=("Arial,60"),width=4,bg="powder blue",command=lambda r=i, c=j:callback(r,c))
        m[i][j].grid(row=i,column=j)

player='X'
stop_game=False
root.mainloop()