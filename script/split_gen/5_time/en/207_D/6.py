def check(s, t):
    for i in range(len(s)):
        for j in range(len(s)):
            if (s[i][0] - s[j][0]) * (t[i][1] - t[j][1]) == (s[i][1] - s[j][1]) * (t[i][0] - t[j][0]):
                return True
    return False
n = int(input())
s = []
t = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))
for i in range(n):
    a, b = map(int, input().split())
    t.append((a, b))
