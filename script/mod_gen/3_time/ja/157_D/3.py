def main():
    N, M, K = map(int, input().split())
    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        F[a-1].append(b-1)
        F[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        B[c-1].append(d-1)
        B[d-1].append(c-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(F[i]) - 1 - len(B[i])
        for j in F[i]:
            if i in B[j]:
                ans[i] -= 1
    print(*ans)

if __name__ == '__main__':
    main()