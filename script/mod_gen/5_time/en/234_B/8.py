def getPoints(n):
    points = []
    for i in range(n):
        point = input().split()
        points.append((int(point[0]),int(point[1])))
    return points

if __name__ == '__main__':
    getPoints()