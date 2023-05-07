def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == K:
        print(1)
    else:
        if A[N - K] == A[N - K - 1]:
            print(1)
        else:
            print((A[N - K] - A[N - K - 1]) // (A[N - K - 1] + 1) + 1)
