def is_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x2 == x3:
        return True
    if x1 == x2 or x2 == x3:
        return False
    if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
        return True
    return False
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if is_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')
