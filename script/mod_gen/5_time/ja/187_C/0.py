def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                return s[1:]
        else:
            if '!' + s in S:
                return s
    return 'satisfiable'

if __name__ == '__main__':
    solve()