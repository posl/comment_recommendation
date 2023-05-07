def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K%2 == 0:
            print(-A[N-K])
        else:
            print(A[N-K])
        return
    A = [abs(a) for a in A]
    A.sort()
    A = [a*(-1) if i%2 == 0 else a for i, a in enumerate(A)]
    A.sort()
    print(A[K-1])
