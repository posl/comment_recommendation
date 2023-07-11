def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S_set = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S_set:
                return s[1:]

if __name__ == '__main__':
    solve()