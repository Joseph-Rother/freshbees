import tkinter as tk
import random

# Rewriting to make code more robust
canvasSize = 7
scale = 30
#region base logic

def neighbors(loc,gridWidth):
    n = []
    if loc%gridWidth < gridWidth-1:
        n.append(loc+1)
    if loc%gridWidth > 0:
        n.append(loc-1)
    if loc>gridWidth:
        n.append(loc-gridWidth)
    if loc<gridWidth*(gridWidth-1):
        n.append(loc+gridWidth)
    return n

def isFullyConnected(roomLocations,hallwayGrid,gridWidth):
    visited = set()
    toVisit = []
    toVisit.append(roomLocations.index(1))
    totalRoomsVisited = 0
    while len(toVisit) > 0 and totalRoomsVisited < sum(roomLocations):
        current = toVisit.pop()
        if current not in visited:
            visited.add(current)
            if roomLocations[current]==1:
                totalRoomsVisited += 1
            for neighbor in neighbors(current,gridWidth):
                if neighbor not in visited and neighbor not in toVisit and (hallwayGrid[neighbor]==1 or roomLocations[neighbor]==1):
                    toVisit.append(neighbor)
    return totalRoomsVisited == sum(roomLocations)

def countConnected(roomLocations,hallwayGrid,gridWidth):
    visited = set()
    toVisit = []
    toVisit.extend(roomLocations)
    connectedCount = 0
    while len(toVisit) > 0:
        current = toVisit.pop()
        if current not in visited:
            visited.add(current)
            connectedCount+=1
            for neighbor in neighbors(current,gridWidth):
                if neighbor not in visited and neighbor not in toVisit and (hallwayGrid[neighbor]==1 or roomLocations[neighbor]==1):
                    toVisit.append(neighbor)
    return connectedCount

#endregion
#region GUI
root = tk.Tk()
grid = tk.Canvas(root, height=canvasSize*scale, width=canvasSize*scale)


def draw(roomLocations,hallwayGrid,gridWidth):
    grid.delete("all")
    for x in range(gridWidth**2):
            if roomLocations[x]:
                grid.create_rectangle((x%gridWidth)*scale, (x//gridWidth)*scale, (x%gridWidth)*scale+scale, (x//gridWidth)*scale+scale, fill="red")
            elif hallwayGrid[x]:
                grid.create_rectangle((x%gridWidth)*scale, (x//gridWidth)*scale, (x%gridWidth)*scale+scale, (x//gridWidth)*scale+scale, fill="black")
            else:
                grid.create_rectangle((x%gridWidth)*scale, (x//gridWidth)*scale, (x%gridWidth)*scale+scale, (x//gridWidth)*scale+scale, fill="white")
    
    
    root.update()

grid.pack()

gg = canvasSize
rc = [0 for i in range(gg**2)]
hw = [0 for i in range(gg**2)]
draw(rc,hw,gg)

#endregion


