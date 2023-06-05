def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] != '!' and s[i] == s[i+1] and s[i+1][0] == '!':
            return s[i]
    return 'satisfiable'
