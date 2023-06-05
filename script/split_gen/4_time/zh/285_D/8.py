def check(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return False
    s_count = {}
    t_count = {}
    for i in range(len(s)):
        if s[i] not in s_count:
            s_count[s[i]] = 1
        else:
            s_count[s[i]] += 1
        if t[i] not in t_count:
            t_count[t[i]] = 1
        else:
            t_count[t[i]] += 1
    for i in range(len(s)):
        if s_count[s[i]] != t_count[s[i]]:
            return False
        if s_count[t[i]] != t_count[t[i]]:
            return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    s_i, t_i = input().split()
    s.append(s_i)
    t.append(t_i)
