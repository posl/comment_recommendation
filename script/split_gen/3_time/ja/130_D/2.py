def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        ans += N - right + 1
        if left == right:
            right += 1
        else:
            sum -= A[left]
    print(ans)
solve()
