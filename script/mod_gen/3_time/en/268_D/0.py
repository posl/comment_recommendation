def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        S[i] = S[i].replace('_', '')
    S = sorted(S)
    for i in range(1, N):
        if S[i-1] in S[i]:
            print(-1)
            return
    for i in range(N):
        T.append(S[i] + '_' * (17 - len(S[i])))
        T.append('_' * (17 - len(S[i])) + S[i])
    for i in range(1, 2 * N):
        if T[i-1] in T[i]:
            print(-1)
            return
    T = sorted(T)
    for i in range(1, 2 * N):
        if T[i-1] in T[i]:
            print(-1)
            return
    for i in range(N):
        for j in range(17):
            if S[i] == T[j]:
                print(T[j + N], end = '')
                break

if __name__ == '__main__':
    main()