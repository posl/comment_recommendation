def check(x1, y1, x2, y2, x3, y3):
    return (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2)
n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check(x[i], y[i], x[j], y[j], x[k], y[k]):
                print("Yes")
                exit()
print("No")
