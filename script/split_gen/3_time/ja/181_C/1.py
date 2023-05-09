def check(x1, y1, x2, y2, x3, y3):
    return (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1)
N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if check(x[i], y[i], x[j], y[j], x[k], y[k]):
                print("Yes")
                exit()
print("No")
