# Shlok Wadhwa, A7, CIS 345, T/Th 10:30am

from tkinter import *
from tkinter import messagebox

player = 1
count = 0
player1_moves = list()
player2_moves = list()


def button_click(i):
    global player, count, buttons, player1_moves, player2_moves
    if player == 1:
        buttons[i].config(text='X', state=DISABLED)
        player1_moves.append(i)
        player = 2
    else:
        buttons[i].config(text='O', state=DISABLED)
        player2_moves.append(i)
        player = 1
    count += 1
    check_for_winner()


def check_for_winner():
    global player1_moves, player2_moves, winning_combinations, count
    c = 0
    for w in winning_combinations:
        c = 0
        for p in player1_moves:
            if p in w:
                c += 1
        if c == 3:
            messagebox.showinfo(title='Winner', message='Player 1: You Win!')
            reset()
            return
        c = 0
        for p in player2_moves:
            if p in w:
                c += 1
        if c == 3:
            messagebox.showinfo(title='Winner', message='Player 2: You Win!')
            reset()
            return
    if count == 9:
        messagebox.showinfo(title='Draw', message='Cats game')
        reset()


def reset():
    global buttons, player, count, player1_moves, player2_moves
    for x in buttons:
        x.config(text='', state=NORMAL)
    player = 1
    count = 0
    player1_moves = list()
    player2_moves = list()


window = Tk()
window.title('Tic-Tac-Toe')
window.geometry('283x200')
window.config(background='black')

button_1 = Button(window, height=4, width=10, text='', command=lambda: button_click(0))
button_1.grid(row=0, column=0)

button_2 = Button(window, height=4, width=10, text='', command=lambda: button_click(1))
button_2.grid(row=0, column=1)

button_3 = Button(window, height=4, width=10, text='', command=lambda: button_click(2))
button_3.grid(row=0, column=2)

button_4 = Button(window, height=4, width=10, text='', command=lambda: button_click(3))
button_4.grid(row=1, column=0)

button_5 = Button(window, height=4, width=10, text='', command=lambda: button_click(4))
button_5.grid(row=1, column=1)

button_6 = Button(window, height=4, width=10, text='', command=lambda: button_click(5))
button_6.grid(row=1, column=2)

button_7 = Button(window, height=4, width=10, text='', command=lambda: button_click(6))
button_7.grid(row=2, column=0)

button_8 = Button(window, height=4, width=10, text='', command=lambda: button_click(7))
button_8.grid(row=2, column=1)

button_9 = Button(window, height=4, width=10, text='', command=lambda: button_click(8))
button_9.grid(row=2, column=2)

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

window.mainloop()
