def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    if N == K:
        print(1)
    else:
        if A[K] == A[K - 1]:
            print(1)
        else:
            print((A[K - 1] - A[K]) // (K - 1) + 1)
