def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        K2 = K // 2
        print((N // K2) ** 3 + ((N + K2) // K2) ** 3)
    else:
        print((N // K) ** 3)
