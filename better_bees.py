import tkinter as tk
import random
# size = 500
# rows = 15
# classNum = 15
# classes = set()
# while len(classes)<classNum:
#     classes.add((size*(random.randint(0,rows-1)+1)/(rows+1),size*(random.randint(0,rows-1)+1)/(rows+1)))
# classes=list(classes)
# top = tk.Tk()
# w = tk.Canvas(top,cursor="circle",height=size,width=size)
# for x in range(len(classes)):
#     w.create_oval(classes[x][0]-10, classes[x][1]-10,classes[x][0]+10, classes[x][1]+10)
# for r in range(rows+1):
#     w.create_line((size*(r)/(rows+1)),0,(size*(r)/(rows+1)),size,fill="#aaaaaa")
# for r in range(rows+1):
#     w.create_line(0,(size*(r)/(rows+1)),size,(size*(r)/(rows+1)),fill="#aaaaaa")
# def on_click(event):
#     print(event.x,event.y)
#     #color the class closest to (event.x, event.y) red
#     closestClass = (float('inf'),float('inf'))
#     for _class in classes:
#         if ((_class[0]-event.x)**2+(_class[1]-event.y)**2) < ((closestClass[0]-event.x)**2+ (closestClass[1]-event.y)**2):
#             closestClass = _class
#     w.create_oval(closestClass[0]-10, closestClass[1]-10,closestClass[0]+10, closestClass[1]+10,fill="red")
#     top.update()
    
        
# w.bind("<Button-1>",on_click)
# w.pack()
# fitnessLabel = tk.Label(top,text="Fitness: 0")
# fitnessLabel.pack(side=tk.BOTTOM)
# top.mainloop()

# Rewriting to make code more robust

#region base logic
gridWidth = 15
gridHeight = 15
numberOfRooms = 5
roomLocations = [] #array of (x, y) room coords
hallwayGrid = [[0 for x in range(gridWidth)] for y in range(gridHeight)]

def neighbors(x, y):
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < gridWidth-1:
        n.append((x+1, y))
    if y > 0:
        n.append((x, y-1))
    if y < gridHeight-1:
        n.append((x, y+1))
    return n
def isFullyConnected():
    visited = set()
    toVisit = []
    toVisit.append(roomLocations[0])
    totalRoomsVisited = 0
    while len(toVisit) > 0 and totalRoomsVisited < len(roomLocations):
        current = toVisit.pop()
        if current not in visited:
            visited.add(current)
            if current in roomLocations:
                totalRoomsVisited += 1
            for neighbor in neighbors(current[0], current[1]):
                if neighbor not in visited and neighbor not in toVisit and (hallwayGrid[neighbor[0]][neighbor[1]] or neighbor in roomLocations):
                    toVisit.append(neighbor)
    return totalRoomsVisited == len(roomLocations)

#endregion
#region GUI
tileSize = 20

root = tk.Tk()
grid = tk.Canvas(root, height=gridHeight*tileSize, width=gridWidth*tileSize)
infoPanel = tk.Frame(root)
isFullyConnectedLabel = tk.Label(infoPanel, text="Fully Connected: False")
def onclick(event):
    #left clicking adds or removes a room
    #right clicking adds or removes a hallway
    if event.num == 1:
        if (event.x//tileSize, event.y//tileSize) in roomLocations:
            roomLocations.remove((event.x//tileSize, event.y//tileSize))
        else:
            roomLocations.append((event.x//tileSize, event.y//tileSize))
    elif event.num == 3:
        hallwayGrid[event.x//tileSize][event.y//tileSize] = not hallwayGrid[event.x//tileSize][event.y//tileSize]
    isFullyConnectedLabel.config(text="Fully Connected: " + str(isFullyConnected()))
    draw()

def draw():
    grid.delete("all")
    for x in range(gridWidth):
        for y in range(gridHeight):
            if hallwayGrid[x][y]:
                grid.create_rectangle(x*tileSize, y*tileSize, x*tileSize+tileSize, y*tileSize+tileSize, fill="black")
            else:
                grid.create_rectangle(x*tileSize, y*tileSize, x*tileSize+tileSize, y*tileSize+tileSize, fill="white")
    for room in roomLocations:
        grid.create_rectangle(room[0]*tileSize, room[1]*tileSize, room[0]*tileSize+tileSize, room[1]*tileSize+tileSize, fill="black")
        grid.create_oval(room[0]*tileSize+tileSize//4, room[1]*tileSize+tileSize//4, room[0]*tileSize+3*tileSize//4, room[1]*tileSize+3*tileSize//4, fill="white")
    root.update()

grid.bind("<Button-1>", onclick)
grid.bind("<Button-3>", onclick)
grid.pack()

infoPanel.pack(side=tk.BOTTOM)
isFullyConnectedLabel.pack(side=tk.LEFT)

draw()
root.mainloop()

#endregion


