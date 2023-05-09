def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return
        A.append(A[-1])
        while A[-1] <= M:
            dfs(A)
            A[-1] += 1
        A.pop()
    dfs([1])
    print(ans)

if __name__ == '__main__':
    main()