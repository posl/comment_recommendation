def solve():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
        else:
            for i in range(A[-1], M+1):
                dfs(A + [i])
    dfs([1])
    print(ans)

if __name__ == '__main__':
    solve()