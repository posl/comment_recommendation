def main():
    N, M, Q = map(int, input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[query[i][1] - 1] - A[query[i][0] - 1] == query[i][2]:
                    score += query[i][3]
            ans = max(ans, score)
            return
        for i in range(A[-1], M + 1):
            dfs(A + [i])
    dfs([1])
    print(ans)

if __name__ == '__main__':
    main()