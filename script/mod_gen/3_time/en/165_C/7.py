def solve(N, M, Q, queries):
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in queries:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(1, M+1):
            if len(A) == 0 or A[-1] <= i:
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    return ans

if __name__ == '__main__':
    solve()