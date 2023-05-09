def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    def dfs(A):
        # すべての数列を作る
        if len(A) == N:
            score = 0
            for a, b, c, d in ABCD:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            return score
        # すべての数列を作る
        res = 0
        for i in range(1, M + 1):
            if len(A) == 0 or A[-1] <= i:
                res = max(res, dfs(A + [i]))
        return res
    print(dfs([]))

if __name__ == '__main__':
    main()