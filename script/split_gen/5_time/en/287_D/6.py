def solve(s,t):
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != '?' and s[i+j] != t[j]:
                break
        else:
            return True
    return False
s = input()
t = input()
n = len(t)
for i in range(n+1):
    if solve(s[:i]+t+s[i:],t):
        print('Yes')
    else:
        print('No')
