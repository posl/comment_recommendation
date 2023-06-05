def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    count = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum < K:
            break
        count += N - right + 1
        sum -= A[left]
    print(count)
solve()
