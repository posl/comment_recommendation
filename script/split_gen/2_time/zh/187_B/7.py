def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
xy = []
for _ in range(n):
    xy.append(tuple(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if abs(xy[i][0]-xy[j][0]) >= abs(xy[i][1]-xy[j][1]):
            ans += 1
print(ans)
