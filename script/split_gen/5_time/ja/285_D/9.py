def check(n, s, t):
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] or t[i] == t[j]:
                return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    a, b = input().split()
    s.append(a)
    t.append(b)
