from Point import Point
import math

pointsArray = []

for i in range(5):
	x = input("Enter x coordinate:")
	y = input("Enter y coordinate:")
	point = Point(x,y)
	pointsArray.append(point)

route = []

x = input("Enter starting x coordinate:")
y = input("Enter starting y coordinate:")
point = Point(x,y)
route.append(point)

while len(pointsArray)!=0:
	min = 1000000
	closestPoint = None
	index = -1
	for i in range(len(pointsArray)):
		dist = math.sqrt(((point.x-pointsArray[i].x)**2) + ((point.y-pointsArray[i].y)**2))
		if dist < min:
			min = dist
			closestPoint = pointsArray[i]
			index = i
	route.append(closestPoint)
	point = pointsArray.pop(index)



for i in route:
	print(str(i))

