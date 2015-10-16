"""
HW5 for GGS650
author: Jiao Ma @GMU

Create four random points and four random rectangles, and find if each
of the point is in any of the rectangles. Write the results to a text file.
"""
import random
## 1. Declare the Point class
class Point:
    def __init__(self, x= 0.0, y= 0.0):
        self.x, self.y = x, y
        
## 2. Declare the Rectangle class
class Rectangle:
    def __init__(self, minX = 0.0, minY = 0.0, maxX = 10.0, maxY = 10.0):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
    def contains(self, point):
        if (point.x >= self.minX) & (point.x <= self.maxX) &\
           (point.y >= self.minY) & (point.y <= self.maxY):
            return True
                   
        else:
            return False

## 3. Generate four points
points = []
def random4Points():
    for i in range(4):
        pointX = 10 * random.random()
        pointY = 10 * random.random()
        points.append(Point(pointX, pointY))
        print points[i].x, points[i].y
    print '\n'

## 4. Generate four rectangles
rectangles = []
def random4Rectangles():
    for j in range(4):
        x1 = 10 * random.random()
        x2 = 10 * random.random()
        while(x1 == x2):
            x1 = 10 * random.random()
        if x1 < x2:
            minX = x1
            maxX = x2
        elif x1 > x2:
            minX = x2
            maxX = x1            
        y1 = 10 * random.random()
        y2 = 10 * random.random()
        while(y1 == y2):
            y1 = 10 * random.random()
        if y1 < y2:
            minY = y1
            maxY = y2
        elif y1 > y2:
            minY = y2
            maxY = y1
        rectangles.append(Rectangle(minX, minY, maxX, maxY))
        print minX, minY, maxX, maxY
    print '\n'

## 5. Check which point is in which rectangle and record the result
def checkPointsInRects():
    resultList = []
    for i in range(len(rectangles)):
        for j in range(len(points)):
            result = rectangles[i].contains(points[j])
            if result == True:
                print 'Point (' + str(points[j].x) + ', ' + str(points[j].y) + ')' + \
                      ' is in rectangle (' + str(rectangles[i].minX) + ', ' + \
                      str(rectangles[i].minY) + ', ' + str(rectangles[i].maxX)\
                      + ', ' + str(rectangles[i].maxY) + ').'
                resultList.append(points[j])

            
random4Points()
random4Rectangles()
checkPointsInRects()

## 6. Write the results to file
f = open('F:\Study\GGS 650\homework\homework5.txt', 'w')
for m in range(len(points)):
    f.write(str(points[m].x) + ', ' + str(points[m].y))
    f.write('\n')
f.write('\n')
for n in range(len(rectangles)):
    f.write(str(rectangles[n].minX) + ', ' + str(rectangles[n].minY) + ', ' + str(rectangles[n].maxX)\
        + ', ' + str(rectangles[n].maxY))
    f.write('\n')
f.write('\n')
for i in range(len(rectangles)):
    for j in range(len(points)):
        result = rectangles[i].contains(points[j])
        if result == True:
            f.write('Point (' + str(points[j].x) + ', ' + str(points[j].y) + ') is in rectangle (' \
        + str(rectangles[i].minX) + ', ' + str(rectangles[i].minY) + ', ' + str(rectangles[i].maxX)\
        + ', ' + str(rectangles[i].maxY) + ').')
            f.write('\n')
f.close()

## 7. Visualize the points and rectangles on a map
from Tkinter import *
root = Tk()
lab = Label(root, text = "HW5__Jiao")
can = Canvas(root, width = 800, height = 600)
for m in range(len(rectangles)):
##    ratioX = (rectangles[0].maxX - rectangles[0].minX)/800
##    ratioY = (rectangles[0].maxY - rectangles[0].minY)/600
##    if ratioX > ratioY:
##        ratio = ratioX
##    else:
##        ratio = ratioY
    ratio = 0.02
    minX = min(rectangles[0].minX, rectangles[1].minX, rectangles[2].minX, rectangles[3].minX)
    maxY = max(rectangles[0].maxY, rectangles[1].maxY, rectangles[2].maxY, rectangles[3].maxY)
    minWinx = (rectangles[m].minX - minX)/ratio
    minWiny = -(rectangles[m].minY - maxY)/ratio
    maxWinx = (rectangles[m].maxX - minX)/ratio
    maxWiny = -(rectangles[m].maxY - maxY)/ratio
    can.create_rectangle(minWinx, minWiny, maxWinx, maxWiny, outline = 'green')
    for n in range(len(points)):
        winx = (points[n].x - minX)/ratio
        winy = -(points[n].y - maxY)/ratio
        can.create_rectangle(winx, winy, winx+7, winy+7, fill = 'red')
    
can.pack()
lab.pack()
root.mainloop()
