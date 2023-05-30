def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    if N == 1:
        if M == 0:
            print(S[0])
            return
        else:
            for t in T:
                if t == S[0]:
                    print(-1)
                    return
            print(S[0])
            return
    if M == 0:
        print(S[0])
        return
    for t in T:
        if t == S[0]:
            print(-1)
            return
    for t in T:
        if t == S[1]:
            print(-1)
            return
    if N == 2:
        print(S[0] + '_' + S[1])
        return
    if N == 3:
        print(S[0] + '_' + S[1] + '_' + S[2])
        return
    if N == 4:
        print(S[0] + '_' + S[2] + '_' + S[1] + '_' + S[3])
        return
    if N == 5:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[1] + '_' + S[3])
        return
    if N == 6:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[1] + '_' + S[3] + '_' + S[5])
        return
    if N == 7:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[6] + '_' + S[1] + '_' + S[3] + '_' + S[5])
        return
    if N == 8:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[6] + '_' + S[1] + '_' + S[3] + '_' + S[5] + '_' + S[7])
        return
solve()
