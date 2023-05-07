def calc_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'inf'
    else:
        return (y2 - y1) / (x2 - x1)
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if calc_slope(x1, y1, x2, y2) == calc_slope(x2, y2, x3, y3):
                print('Yes')
                exit()
print('No')
