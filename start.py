from tkinter import *
from tkinter import ttk
import os
def start_game():
    print("Starting game...")
    os.system('cmd /c "startGame.bat"')

def exit():
    print("Exiting...")
    root.destroy()

def ttr():
    #open the file how-to-play.txt in notepad
    os.system('cmd /c "notepad.exe how-to-play.txt"')

root = Tk()
root.title("Start JitterCube")
root.resizable(False, False)
root.geometry("300x300")
start = ttk.Button(
   root, 
   text="Start Game", 
   command=start_game
)
start.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

ttr = ttk.Button(
   root, 
   text="How to play", 
   command=ttr
)
ttr.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

exitButtom = ttk.Button(
   root, 
   text="Exit", 
   command=exit
)
exitButtom.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
