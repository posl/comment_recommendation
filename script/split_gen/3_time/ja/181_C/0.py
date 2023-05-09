def check(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if check(x1, y1, x2, y2, x3, y3):
                print('Yes')
                exit()
print('No')
