def main():
    N, K = map(int, input().split())
    print((N-K+2)*(K-1) % (10**9+7))
