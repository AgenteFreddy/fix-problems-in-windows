import os
import tkinter as tk

def filebat():
    open = os.startfile("FixWindows.bat")

def main():
    win = tk.Tk()
    win.title('The FixWindows')
    win.geometry('500x500')

    text = tk.Label(win,text='Welcome to FixWindows')
    text.pack()

    text2 = tk.Label(win,text='The FixWindows is a Software for resolve many problems in your Windows')
    text2.pack()

    button = tk.Button(win, text='Click', command=filebat)
    button.pack()

    win.mainloop()
main()



