def solve(n, s):
    s1 = set()
    s2 = set()
    for i in range(n):
        if s[i][0] == '!':
            s1.add(s[i][1:])
        else:
            s2.add(s[i])
    for i in s2:
        if i in s1:
            return i
    return 'satisfiable'
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(solve(n, s))
