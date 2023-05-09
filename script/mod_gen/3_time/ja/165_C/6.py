def main():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for A in dfs(N, M):
        score = 0
        for a, b, c, d in query:
            if A[b-1] - A[a-1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()