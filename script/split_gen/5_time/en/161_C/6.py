def main():
    N, K = map(int, input().split())
    if N == 0:
        print(0)
        return
    N = N % K
    print(min(N, K-N))
