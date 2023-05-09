def main():
    N, M, Q = map(int, input().split())
    L = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        L.append((a-1, b, c, d))
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in L:
                if A[b] - A[a] == c:
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