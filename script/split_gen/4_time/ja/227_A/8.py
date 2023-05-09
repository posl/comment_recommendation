def problem227_a():
    N, K, A = map(int, input().split())
    print((K - 1 + A - 1) % N + 1)
    return
