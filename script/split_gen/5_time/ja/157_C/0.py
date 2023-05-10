def check(n, s, c):
    for i in range(len(s)):
        if n[s[i]-1] != c[i]:
            return False
    return True
n, m = map(int, input().split())
s = []
c = []
for _ in range(m):
    _s, _c = map(int, input().split())
    s.append(_s)
    c.append(_c)
