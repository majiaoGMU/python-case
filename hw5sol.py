import random

# define the biggest number of the coordinates for points and rectangles so that we can change once and use many times
BIGGESTNUMBER = 800

# define the Point class
class Point:
    def __init__(self, x, y): # initializing the function by passing in values
        self.x, self.y = x, y

# define the rectangle class
class Rectangle:
    def __init__(self, minx, miny, maxx, maxy): #initializing the function by passing in values
        self.minx, self.miny, self.maxx, self.maxy = minx, miny, maxx, maxy

        while (self.minx==self.maxx):
            self.maxx = random.randint(0, BIGGESTNUMBER)
        while (self.miny==self.maxy):
            self.maxy = random.randint(0, BIGGESTNUMBER)
        if self.minx > self.maxx:
            temp = self.minx
            self.minx = self.maxx
            self.maxx = temp
        if self.miny > self.maxy:
            temp = self.miny
            self.miny = self.maxy
            self.maxy = temp  
  
    def pointinside(self, point): # check if a point is inside the rectangle
        if ((self.maxx > point.x > self.minx) & (self.maxy > point.y > self.miny)):
            return True 
        else:
            return False  

points = []
outputFile = open("hw5results.txt", "w") # open the file to write result to

for i in range(0,4): # generate four points
    point = Point(random.randint(0,BIGGESTNUMBER),random.randint(0,BIGGESTNUMBER))
    points.append(point)
    outputFile.write("The "+str(i)+ "th point is ("+ str(points[i].x) + ',' + str(points[i].y)+")\n")

rectangles = []
for i in range(0,4): # generate four rectangles
    rectangle = Rectangle(random.randint(0, BIGGESTNUMBER), random.randint(0, BIGGESTNUMBER), random.randint(0, BIGGESTNUMBER), random.randint(0, BIGGESTNUMBER))
    rectangles.append(rectangle)
    outputFile.write("The "+str(i)+ "th rectangle is ("+ str(rectangles[i].minx) + ',' + str(rectangles[i].miny) + ',' + str(rectangles[i].maxx) + ',' + str(rectangles[i].maxy)+")\n")


#loop through points and rectangle to check results
for point in points: 
    for rectangle in rectangles:
        if (rectangle.pointinside(point)):
            outputFile.write('This point '+str(points.index(point))+' is inside the rectangle ' +str(rectangles.index(rectangle))+ "\n")
        else:
            outputFile.write('This point '+str(points.index(point))+' is not inside the rectangle '+str(rectangles.index(rectangle))+ '\n')

outputFile.close()

# visualize the data using Tkinter
from Tkinter import *

root = Tk()
can = Canvas(root, width = 800, height = 800)

for i in range(4):
    rectangle = rectangles[i]
    point = points[i]
    can.create_rectangle(rectangle.minx,rectangle.miny, rectangle.maxx, rectangle.maxy)
    can.create_text(point.x, point.y, text="o")
can.pack()		
root.mainloop()
