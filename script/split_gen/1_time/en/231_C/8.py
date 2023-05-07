def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))
import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = []
for i in range(q):
    x.append(int(input()))
solve(n, q, a, x)
