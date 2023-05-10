def main():
    N, K = map(int, input().split())
    if N < K:
        print(N)
    else:
        print(N % K)
