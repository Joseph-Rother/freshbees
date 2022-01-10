import tkinter as tk
import random
size = 500
rows = 15
classNum = 15
classes = set()
while len(classes)<classNum:
    classes.add((size*(random.randint(0,rows-1)+1)/(rows+1),size*(random.randint(0,rows-1)+1)/(rows+1)))
classes=list(classes)
top = tk.Tk()
w = tk.Canvas(top,cursor="circle",height=size,width=size)
for x in range(len(classes)):
    w.create_oval(classes[x][0]-10, classes[x][1]-10,classes[x][0]+10, classes[x][1]+10)
for r in range(rows+1):
    w.create_line((size*(r)/(rows+1)),0,(size*(r)/(rows+1)),size,fill="#aaaaaa")
for r in range(rows+1):
    w.create_line(0,(size*(r)/(rows+1)),size,(size*(r)/(rows+1)),fill="#aaaaaa")

w.pack()
top.mainloop()