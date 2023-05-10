def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    A = []
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(A[-1] if A else 1, M+1):
            A.append(i)
            dfs(A)
            A.pop()
    dfs(A)
    print(ans)
