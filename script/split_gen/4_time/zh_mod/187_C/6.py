def solve():
    n = int(input())
    s = [input() for i in range(n)]
    t = set()
    for i in range(n):
        if s[i][0] == '!':
            t.add(s[i][1:])
        else:
            t.
