def main():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for i in range(Q)]
    def dfs(A):
        if len(A) == N:
            score = 0
            for a, b, c, d in query:
                if A[b-1] - A[a-1] == c:
                    score += d
            return score
        else:
            for i in range(A[-1], M+1):
                A.append(i)
                yield from dfs(A)
                A.pop()
    ans = 0
    for i in range(1, M+1):
        ans = max(ans, max(dfs([i])))
    print(ans)

if __name__ == '__main__':
    main()