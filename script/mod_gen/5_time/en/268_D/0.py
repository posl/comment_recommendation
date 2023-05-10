def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == S[j]:
                print(-1)
                return
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if T[i] == T[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return
    for i in range(M):
        for j in range(N):
            if T[i] in S[j]:
                print(-1)
                return
    for i in range(N):
        for j in range(M):
            if S[i] + '_' + T[j] not in T and T[j] + '_' + S[i] not in T:
                print(S[i] + '_' + T[j])
                return
main()

if __name__ == '__main__':
    main()