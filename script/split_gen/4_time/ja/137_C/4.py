def count(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
n = int(input())
s = []
for i in range(n):
    s.append(input())
d = {}
for i in range(n):
    d[i] = count(s[i])
from itertools import combinations
ans = 0
for c in combinations(range(n), 2):
    if d[c[0]] == d[c[1]]:
        ans += 1
print(ans)
