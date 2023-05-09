def count(s):
    c = [0] * 26
    for i in range(len(s)):
        c[ord(s[i]) - ord('a')] += 1
    return tuple(c)
n = int(input())
s = [input() for _ in range(n)]
d = {}
for i in range(n):
    c = count(s[i])
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)

if __name__ == '__main__':
    count()