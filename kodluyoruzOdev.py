#Fatma Özdemir

import math

x1 = int(input("x1 sayisini giriniz: "))
x2 = int(input("x2 sayisini giriniz: "))
y1 = int(input("y1 sayisini giriniz: "))
y2 = int(input("y2 sayisini giriniz: "))

points = [(x1,y1) , (x2,y2)]

def euclideanDistance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print("Minimum Mesafe: " , min_distance)