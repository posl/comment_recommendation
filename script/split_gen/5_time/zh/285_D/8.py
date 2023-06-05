def check(s, t):
    if s == t:
        return False
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] == t[i]:
            return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    s_i, t_i = input().split()
    s.append(s_i)
    t.append(t_i)
for i in range(n):
    for j in range(i+1, n):
        if check(s[i], s[j]) == False:
            return False
        if check(t[i], t[j]) == False:
            return False
    for j in range(n):
        if check(s[i], t[j]) == False:
            return False
        if check(t[i], s[j]) == False:
            return False
return True
