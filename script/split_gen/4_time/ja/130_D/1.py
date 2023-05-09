def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + A[right] < K:
            sum += A[right]
            right += 1
        #print(right, sum)
        ans += right - left
        if right == left:
            right += 1
        else:
            sum -= A[left]
    print(ans)
