# Created by Eli Foster

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def method():
    tkMessageBox.showinfo("swerve", "Hello Noob")

button = Tkinter.Button(top, text ="Noob", command = method)

canvas = Tkinter.Canvas(top, bg="red", height=250, width=250)
coord = 10, 50, 240, 210
arc = canvas.create_oval(coord, fill="blue")


button.pack()
canvas.pack()
top.mainloop()