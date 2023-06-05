def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    cnt = 0
    right = 0
    for left in range(N):
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum == K:
            cnt += 1
        if left == right:
            right += 1
        else:
            sum -= A[left]
    print(cnt)
