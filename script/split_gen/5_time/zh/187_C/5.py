def solve():
    N = int(input())
    S = [input() for i in range(N)]
    S = set(S)
    for s in S:
        if '!' + s in S:
            return s
    return 'satisfiable'
print(solve())
