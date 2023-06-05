def main():
    N, L = map(int, input().split())
    if L > 0:
        print((N * L + N * (N - 1)) // 2 - L)
    elif N + L <= 0:
        print((N * L + N * (N - 1)) // 2 - L - N + 1)
    else:
        print((N * L + N * (N - 1)) // 2)
