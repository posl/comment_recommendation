def main():
    N, K = map(int, input().split())
    if N > K:
        N = N % K
    if N > abs(N-K):
        N = abs(N-K)
    print(N)
main()
