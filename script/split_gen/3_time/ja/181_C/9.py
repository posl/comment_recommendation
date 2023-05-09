def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
