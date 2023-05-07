def check(n, s, c):
    if n[s] == c:
        return True
    else:
        return False
n, m = map(int, input().split())
s = [0] * m
c = [0] * m
for i in range(m):
    s[i], c[i] = map(int, input().split())
