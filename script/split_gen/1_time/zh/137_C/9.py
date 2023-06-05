def hash(s):
    h = 0
    for i in range(0, len(s)):
        h = h * 26 + ord(s[i]) - ord('a')
    return h
n = int(input())
d = {}
for i in range(0, n):
    s = input()
    h = hash(s)
    if h in d:
        d[h] += 1
    else:
        d[h] = 1
ans = 0
for k in d:
    v = d[k]
    ans += v * (v - 1) // 2
print(ans)
