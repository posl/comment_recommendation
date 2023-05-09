def check(x1, y1, x2, y2, x3, y3):
    if x1 - x2 == 0:
        if x1 - x3 == 0:
            return True
        else:
            return False
    else:
        if x1 - x3 == 0:
            return False
        else:
            if (y1 - y2) / (x1 - x2) == (y1 - y3) / (x1 - x3):
                return True
            else:
                return False
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if check(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')
