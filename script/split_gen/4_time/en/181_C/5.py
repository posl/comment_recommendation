def check_line(x1, y1, x2, y2, x3, y3):
    if (x1 == x2) and (x2 == x3):
        return True
    elif (y1 == y2) and (y2 == y3):
        return True
    elif ((x1 - x2) != 0) and ((x2 - x3) != 0):
        if ((y1 - y2) / (x1 - x2)) == ((y2 - y3) / (x2 - x3)):
            return True
    return False
n = int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')
