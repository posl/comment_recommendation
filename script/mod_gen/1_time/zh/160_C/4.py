def solve(K, N, A):
    A.append(K)
    A.sort()
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + 1] - A[i])
    return K - ans
K, N = map(int, input().split())
A = list(map(int, input().split()))
print(solve(K, N, A))
