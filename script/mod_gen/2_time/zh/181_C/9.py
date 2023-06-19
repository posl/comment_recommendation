def isLine(x1, y1, x2, y2, x3, y3):
    if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return True
    else:
        return False
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
res = "No"
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if isLine(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                res = "Yes"
print(res)

if __name__ == '__main__':
    isLine()