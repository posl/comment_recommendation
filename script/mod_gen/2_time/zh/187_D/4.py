def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [s.lstrip('!') for s in S]
    S = set(S)
    for s in S:
        if '!' + s in S:
            return s
    return 'satisfiable'

if __name__ == '__main__':
    solve()