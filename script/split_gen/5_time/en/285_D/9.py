def check(s, t, n):
    for i in range(n):
        if s[i] == t[i]:
            return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    si, ti = map(str, input().split())
    s.append(si)
    t.append(ti)
