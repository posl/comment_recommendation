def solve(N, K, A):
    ans = 0
    sum = 0
    r = 0
    for l in range(N):
        while sum < K and r < N:
            sum += A[r]
            r += 1
        if sum < K:
            break
        ans += N - r + 1
        sum -= A[l]
    return ans
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, K, A))
