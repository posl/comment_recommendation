def lcm(x, y):
    return (x * y) // math.gcd(x, y)
import math
import collections
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))
a = list(map(lambda x: lcm(x, 1), a))
a = list(map(lambda x: x // 1, a))
a = list(map(lambda x: x // 2, a))
a = list(map(lambda x: x // 1, a))
c = collections.Counter(a)
c = sorted(c.items(), key=lambda x:x[0])
c = list(map(lambda x: x[1], c))
ans = 0
for i in range(1, m + 1):
    d = 0
    for j in c:
        if i % j == 0:
            d += 1
    if d == len(c):
        ans += 1
print(ans)

if __name__ == '__main__':
    lcm()