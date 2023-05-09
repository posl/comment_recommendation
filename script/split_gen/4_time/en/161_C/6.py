def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print(min(N % K, K - N % K))
