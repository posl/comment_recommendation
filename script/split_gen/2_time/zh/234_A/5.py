def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    sum = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum == K:
            ans += 1
        if r == l:
            r += 1
        else:
            sum -= A[l]
    print(ans)
