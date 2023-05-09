def anagram(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d
n = int(input())
s = [input() for _ in range(n)]
d = {}
for i in range(n):
    a = anagram(s[i])
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
ans = 0
for k in d:
    ans += d[k] * (d[k] - 1) // 2
print(ans)
