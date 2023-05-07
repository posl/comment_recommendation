def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i] - 1].append(B[i] - 1)
    used = [False] * N
    ans = []
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        ans.append(i)
        for j in G[i]:
            if used[j]:
                print(-1)
                return
            used[j] = True
            ans.append(j)
    print(*[i + 1 for i in ans])

if __name__ == '__main__':
    main()