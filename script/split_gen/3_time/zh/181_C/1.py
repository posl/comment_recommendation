def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            dx1 = x[j] - x[i]
            dy1 = y[j] - y[i]
            dx2 = x[k] - x[i]
            dy2 = y[k] - y[i]
            if dx1 * dy2 == dx2 * dy1:
                print('Yes')
                exit()
print('No')
