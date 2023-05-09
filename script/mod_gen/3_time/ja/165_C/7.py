def main():
    N, M, Q = map(int, input().split())
    # N, M, Q = 10, 10, 1
    # a, b, c, d = 1, 10, 9, 1
    a, b, c, d = [0]*Q, [0]*Q, [0]*Q, [0]*Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        # a[i], b[i], c[i], d[i] = 1, 10, 9, 1
    ans = 0
    # A = [0]*N
    A = [0]*N
    def dfs(i):
        global ans
        if i == N:
            score = 0
            for j in range(Q):
                if A[b[j]-1] - A[a[j]-1] == c[j]:
                    score += d[j]
            ans = max(ans, score)
            return
        for j in range(1, M+1):
            A[i] = j
            dfs(i+1)
    dfs(0)
    print(ans)

if __name__ == '__main__':
    main()