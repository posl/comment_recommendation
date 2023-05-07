def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[-1] = M
    ans = 0
    for i in range(1, N-1):
        A[i] = i + 1
    def dfs(A, i):
        global ans
        if i == N:
            score = 0
            for j in range(Q):
                a, b, c, d = map(int, input().split())
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for j in range(A[i-1], M+1):
            A[i] = j
            dfs(A, i+1)
    dfs(A, 1)
    print(ans)

if __name__ == '__main__':
    main()