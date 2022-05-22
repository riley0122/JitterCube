from struct import pack
from tkinter import *
from tkinter import ttk
import json
import os
def OpenMenu():
    print("Opening menu...")
    os.system('cmd /c "run.bat"')
    #close the window
    root.destroy()

def exit():
    print("Exiting...")
    root.destroy()

root = Tk()
root.title("JitterCube Options")
root.resizable(False, False)
#set the icon to ./logo.ico
root.iconbitmap('./logo.ico')
root.geometry("600x300")
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

tomenu = ttk.Button(
   root, 
   text="Main Menu", 
   command=OpenMenu
)
tomenu.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#get filepath
filepath = os.path.dirname(os.path.realpath(__file__))
with open(filepath+'/options.json', 'r') as f:
    optionsString = Text(root, height=5)
    optionsString.pack()
    optionsString.config(state="normal")
    optionsString.insert(END,f.read())
    
def save():
    with open(filepath+'/options.json', 'w') as f:
        y = json.loads(optionsString.get("1.0",END))
        f.write(json.dumps(y, indent=4))
    with open(filepath+'/options.json', 'r') as f:
        options = f.read()
        #get volume from options
        x = json.loads(options)
        volume = x['volume']
        #if volume is less than 0 or higher than 1 set it to 1
        if volume < 0 or volume > 1:
            volume = 1
        speed = x['speed']
    #set volume
    with open(filepath+'/options.json', 'w') as f:
        f.write(json.dumps(
            {
                'speed': speed,
                'volume': volume
            }))
        f.close()

set = ttk.Button(
    root,
    text="Save Options",
    command=save
)
set.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
