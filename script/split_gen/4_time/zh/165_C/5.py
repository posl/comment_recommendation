def solve():
    N, M, Q = map(int, input().split())
    query = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        query.append((a, b, c, d))
    def dfs(A):
        if len(A) == N:
            score = 0
            for a, b, c, d in query:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            return score
        else:
            max_score = 0
            if len(A) == 0:
                start = 1
            else:
                start = A[-1]
            for n in range(start, M + 1):
                max_score = max(max_score, dfs(A + [n]))
            return max_score
    print(dfs([]))
solve()
