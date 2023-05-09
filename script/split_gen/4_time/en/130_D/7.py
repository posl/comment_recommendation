def problem():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        total = 0
        for j in range(i, N):
            total += A[j]
            if total >= K:
                count += N - j
                break
    print(count)
