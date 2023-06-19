def main():
    N, M, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    def dfs(A, B):
        nonlocal ans
        if len(B) == N:
            score = 0
            for a, b, c, d in A:
                if B[b - 1] - B[a - 1] == c:
                    score += d
            ans = max(ans, score)
        else:
            for i in range(B[-1] if B else 1, M + 1):
                dfs(A, B + [i])
    dfs(A, [])
    print(ans)
