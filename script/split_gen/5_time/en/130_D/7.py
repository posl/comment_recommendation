def solve(N, K, A):
    # write your code here
    ans = 0
    sum = 0
    left = 0
    for right in range(N):
        sum += A[right]
        while sum >= K:
            ans += N - right
            sum -= A[left]
            left += 1
    return ans
