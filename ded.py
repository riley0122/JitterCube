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
root.title("You are have ded")
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

text1 = Text(root, height=1, width=13)
text1.pack()
text1.config(state="normal")
text1.insert(END,"You have died")
text1.configure(state='disabled')

#load highscore
with open('highscore.csv', 'r') as f:
    highscore = int(f.read())
    highscoreString = str(highscore)
    hstext = Text(root, height=1, width=15)
    hstext.pack()
    hstext.config(state="normal")
    hstext.insert(END,"Highscore: "+highscoreString)
    hstext.configure(state='disabled')

start = ttk.Button(
   root, 
   text="Restart", 
   command=start_game
)
start.pack(
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
