def main():
    N, K, A = map(int, input().split())
    if K <= N:
        print(K)
    else:
        print(N - (K - N) % (N - A + 1))
