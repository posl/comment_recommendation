def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [int(input()) for i in range(N)]
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total + A[right] < K:
            total += A[right]
            right += 1
        ans += N - right
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)
solve()
