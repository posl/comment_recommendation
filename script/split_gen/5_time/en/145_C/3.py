def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        total += distance(xy[i][0], xy[i][1], xy[j][0], xy[j][1])
print(total/math.factorial(n))
