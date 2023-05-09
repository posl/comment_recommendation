def isConvex(points):
    #Check the number of points
    if len(points) != 4:
        return False
    #Check the number of unique points
    if len(set(points)) != 4:
        return False
    #Check the number of unique x coordinates
    if len(set([point[0] for point in points])) != 4:
        return False
    #Check the number of unique y coordinates
    if len(set([point[1] for point in points])) != 4:
        return False
    #Check if the points are colinear
    for i in range(4):
        if (points[i][0] - points[(i+1)%4][0])*(points[i][1] - points[(i+2)%4][1]) == (points[i][0] - points[(i+2)%4][0])*(points[i][1] - points[(i+1)%4][1]):
            return False
    #Check the angles
    for i in range(4):
        if (points[i][0] - points[(i+1)%4][0])*(points[i][0] - points[(i+2)%4][0]) + (points[i][1] - points[(i+1)%4][1])*(points[i][1] - points[(i+2)%4][1]) < 0:
            return False
    return True
points = []
for i in range(4):
    points.append(tuple(map(int, input().split())))
print("Yes" if isConvex(points) else "No")

if __name__ == '__main__':
    isConvex()