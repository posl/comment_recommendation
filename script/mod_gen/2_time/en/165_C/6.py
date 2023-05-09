def main():
    N, M, Q = map(int, input().split())
    A = [1] * N
    ans = 0
    def dfs(i):
        nonlocal ans
        if i == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return
        for j in range(A[i - 1], M + 1):
            A[i] = j
            dfs(i + 1)
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    dfs(1)
    print(ans)

if __name__ == '__main__':
    main()