def main():
    N, K = map(int, input().split())
    while N >= K:
        N = N % K
        if N > K/2:
            N = abs(N - K)
    print(N)
