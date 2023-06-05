def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
