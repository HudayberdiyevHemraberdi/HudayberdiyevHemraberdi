import numpy as np
import matplotlib.pyplot as plt

def is_convex(points):
    def direction(p1, p2, p3):
        return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

    n = len(points)
    if n < 3:
        return False
    
    sign = None
    for i in range(n):
        d = direction(points[i], points[(i+1)%n], points[(i+2)%n])
        if d == 0:
            continue
        if sign is None:
            sign = d > 0
        elif sign != (d > 0):
            return False
    
    return True

points = np.array([[3, 1], [2, 0], [-1, -2], [0, 0], [2, 1]])

if is_convex(points):
    print("Полигон выпуклый")
else:
    print("Полигон невыпуклый")

plt.figure()
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(points[:,0], points[:,1], 'bo-')
plt.fill(points[:,0], points[:,1], 'b', alpha=0.3)
plt.show()
