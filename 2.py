import numpy as np
import matplotlib.pyplot as plt

def is_inside_polygon(polygon, point):
    n = len(polygon)
    inside = False
    
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i+1) % n]
        
        if (p1[1] <= point[1] and p2[1] > point[1]) or (p1[1] > point[1] and p2[1] <= point[1]):
            if point[0] < (p2[0] - p1[0]) * (point[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
                inside = not inside
        
    return inside

polygon = np.array([[6, 0], [2, -2], [-1, -2], [-4, 1], [0, 5], [2, 6]])
points = np.array([[2, -1], [-1, 2], [-5, 2], [-3, -1], [4, 3]])

plt.figure()
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(polygon[:,0], polygon[:,1], 'bo-')
plt.fill(polygon[:,0], polygon[:,1], 'b', alpha=0.3)

for point in points:
    if is_inside_polygon(polygon, point):
        plt.plot(point[0], point[1], 'go')
    else:
        plt.plot(point[0], point[1], 'ro')

plt.show()
