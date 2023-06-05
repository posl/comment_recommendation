def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + a[right] < K:
            sum += a[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            sum -= a[left]
    print(ans)
