def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            A = V[:i] + V[N - j:]
            A.sort()
            tmp = sum(A)
            for k in range(min(K - i - j, i + j)):
                if A[k] < 0:
                    tmp -= A[k]
            ans = max(ans, tmp)
    print(ans)
