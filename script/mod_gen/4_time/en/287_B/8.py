def main():
    # input
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # compute
    S.sort()
    T.sort()
    ans = 0
    i = 0
    j = 0
    while i < N and j < M:
        if S[i] == T[j]:
            ans += 1
            i += 1
            j += 1
        elif S[i] < T[j]:
            i += 1
        else:
            j += 1
    # output
    print(ans)

if __name__ == '__main__':
    main()