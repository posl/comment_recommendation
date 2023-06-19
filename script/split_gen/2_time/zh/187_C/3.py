def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S1.add(s[1:])
        else:
            S2.add(s)
    for s in S1:
        if s in S2:
            return s
    return 'satisfiable'
print(solve())
