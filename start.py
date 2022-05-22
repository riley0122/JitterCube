from tkinter import *
from tkinter import ttk
import os
def start_game():
    print("Starting game...")
    os.system('cmd /c "startGame.bat"')
    #close the window
    root.destroy()

def exit():
    print("Exiting...")
    root.destroy()

def ttr():
    #open the file how-to-play.txt in notepad
    os.system('cmd /c "notepad.exe how-to-play.txt"')

root = Tk()
root.title("Start JitterCube")
root.resizable(False, False)
#set the icon to ./logo.ico
root.iconbitmap('./logo.ico')
root.geometry("300x300")
#set the background colour to #ffffff
root.configure(background="#ffffff")
#load the image logo.png
logo = PhotoImage(file='./logo.png')
#display the logo
logo_label = Label(root, image=logo)
logo_label.pack()
text = Text(root, height=1, width=10)
text.pack()
text.config(state="normal")
text.insert(END,"JitterCube")
text.configure(state='disabled')

#load highscore
with open('highscore.csv', 'r') as f:
    highscore = int(f.read())
    highscoreString = str(highscore)
    hstext = Text(root, height=1, width=15)
    hstext.pack()
    hstext.config(state="normal")
    hstext.insert(END,"Highscore: "+highscoreString)
    hstext.configure(state='disabled')

def options():
    #open the file options.txt in notepad
    os.system('cmd /c "options.bat"')
    #close the window
    root.destroy()

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

options = ttk.Button(
    root,
    text="Options",
    command=options
)
options.pack(
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
