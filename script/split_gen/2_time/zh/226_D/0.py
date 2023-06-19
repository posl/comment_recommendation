def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
