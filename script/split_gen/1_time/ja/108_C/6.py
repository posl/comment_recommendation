def solve():
    N, K = map(int, input().split())
    if K % 2 == 0:
        K_ = K // 2
        print((N // K_) ** 3 + ((N + K_) // K_) ** 3)
    else:
        print((N // K) ** 3)
