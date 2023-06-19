def f(s):
    return set(s)
n, k = map(int, input().split())
s = [input() for _ in range(n)]
ans = 0
for i in range(1 << n):
    if bin(i).count('1') != k:
        continue
    t = set()
    for j in range(n):
        if i >> j & 1:
            t |= f(s[j])
    if len(t) == k:
        ans = max(ans, bin(i).count('1'))
print(ans)
