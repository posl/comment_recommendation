def check(x,y,h):
    for i in range(n):
        if h != max(H - abs(x - X[i]) - abs(y - Y[i]), 0):
            return False
    return True
n = int(input())
X = [0] * n
Y = [0] * n
H = [0] * n
for i in range(n):
    X[i], Y[i], H[i] = map(int, input().split())
for i in range(n):
    if H[i] != 0:
        break
for x in range(101):
    for y in range(101):
        h = H[i] + abs(x - X[i]) + abs(y - Y[i])
        if check(x,y,h):
            print(x,y,h)
            break
