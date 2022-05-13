from tkinter import *
from tkinter import ttk
import os
def start_game():
    print("Starting game...")
    os.system('cmd /c "startGame.bat"')

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
root.mainloop()
