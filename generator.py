from Tkinter import *
import random as r

class Point:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;
		self.visible = 1;

	def insideCircle(self, centerPoint,radius):
		squareDist = (centerPoint.x-self.x)**2 + (centerPoint.y-self.y)**2
		return squareDist < radius**2

	def removePoint(self, canvas):
		self.visible = 0;
		canvas.create_oval(self.x, self.y, self.x, self.y, outline='white')

class Vector:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;



def getVector(p0, p1):
	return Vector(p1.x-p0.x, p1.y-p0.y)

def averageVector(vectors):
	x = 0
	y = 0
	i = 0
	for v in vectors:
		x += v.x
		y += v.y
		i +=1
	
	return Vector( round(x/i), round(y/i) )

def drawLine(point, vector, canvas, lineWidth):
	w.create_line(point.x, point.y, point.x + vector.x, point.y + vector.y, width=lineWidth)
	
		

def findNextSeed(seed, jumps, canvas, lineWidth):
	vectors = []
	for p in points:
		if (p.visible == 0):
			continue
		if( p.insideCircle(seed, searchRadius) ):
			p.removePoint(canvas)
			vectors.append( getVector(seed, p) )
	#print len(vectors)
	#print 'old : ' + str(seed.x) + ' ' + str(seed.y)
	if (len(vectors) != 0 and jumps != 0):
		v = averageVector(vectors)
		#print 'new : ' + str(v.x) + ' ' + str(v.y)
		seed.removePoint(canvas)
		drawLine(seed, v, canvas, lineWidth)
		findNextSeed(Point(seed.x + v.x, seed.y + v.y), jumps-1, canvas, lineWidth)
	

noofPoints = 1500
noofSeeds = 10

#minSeedJumps = 1
maxSeedJumps = 1

searchRadius = 200

canvasWidth = 1000
canvasHeight = 1000

points = []
seeds = []
master = Tk()



#############
### START ###
#############
w = Canvas(master, width=canvasWidth, height=canvasHeight, bg='white')
w.pack()


#generate points
for i in range(noofPoints):
	p = Point(r.randrange(0, canvasWidth), r.randrange(0, canvasHeight))
	w.create_oval(p.x, p.y, p.x, p.y)
	points.append(p)
#generate seeds
for i in range(noofSeeds):
	p = Point(r.randrange(0, canvasWidth), r.randrange(0, canvasHeight))
	w.create_oval(p.x, p.y, p.x, p.y, outline='red')
	seeds.append(p)


# Find points within maxRadius of each seedpoint
# Average the vector between seed and points to create a new seed.
# Connect the seeds with a line

for s in seeds:
	jumps = r.randrange(1, maxSeedJumps+1)
	findNextSeed(s, jumps, w, 5)
		
	



#delete all remaining points
for p in points:
	if (p.visible == 1):
		p.removePoint(w)
for s in seeds:
	if (s.visible == 1):
		s.removePoint(w)
		

#draw black borders

#top
#w.create_line(0, 0, 1500, 0, width=10)
#left
#w.create_line(0, 0, 0, 900, width=10)
#right
#w.create_line(1500, 0, 1500, 900, width=10)
#bottom
#w.create_line(0, 900, 1500, 900, width=10)

#w.create_line(100, 100, 400, 300, width=5)
mainloop()










