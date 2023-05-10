def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S_set:
                return s[1:]
        else:
            if '!' + s in S_set:
                return s
    return 'satisfiable'
print(solve())

if __name__ == '__main__':
    solve()