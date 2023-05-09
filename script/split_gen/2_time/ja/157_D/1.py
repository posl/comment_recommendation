def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    F = [set() for _ in range(N)]
    B = [set() for _ in range(N)]
    for a, b in AB:
        F[a - 1].add(b - 1)
        F[b - 1].add(a - 1)
    for c, d in CD:
        B[c - 1].add(d - 1)
        B[d - 1].add(c - 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(F[i]) - 1
        for j in F[i]:
            if i in F[j]:
                ans[i] -= 1
        for j in B[i]:
            if j in F[i]:
                ans[i] -= 1
    print(*ans)
