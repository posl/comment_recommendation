def check_order(n, s, t):
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == t[j] and s[j] == t[i]:
                return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    s_i, t_i = input().split()
    s.append(s_i)
    t.append(t_i)
