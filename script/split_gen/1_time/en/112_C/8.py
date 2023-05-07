def check(x,y,h):
    for i in range(N):
        if max(h-abs(x-xi[i])-abs(y-yi[i]),0) != hi[i]:
            return False
    return True
N = int(input())
xi = []
yi = []
hi = []
for i in range(N):
    x,y,h = map(int,input().split())
    xi.append(x)
    yi.append(y)
    hi.append(h)
for i in range(N):
    if hi[i] != 0:
        break
x = xi[i]
y = yi[i]
h = hi[i]
for cx in range(101):
    for cy in range(101):
        if check(cx,cy,h):
            print(cx,cy,h)
            exit()
