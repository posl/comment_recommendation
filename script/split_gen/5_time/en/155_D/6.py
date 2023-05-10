def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    min_value = -10**18 - 1
    max_value = 10**18 + 1
    while max_value - min_value > 1:
        mid = (max_value + min_value) // 2
        count = 0
        j = N - 1
        for i in range(N):
            while j >= 0 and A[i] * A[j] <= mid:
                j -= 1
            count += N - 1 - j
        if count >= K:
            max_value = mid
        else:
            min_value = mid
    print(max_value)
