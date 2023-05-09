def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1])
    elif A[N-1] <= 0:
        if K % 2 == 0:
            print(abs(A[N-K]))
        else:
            print(A[N-K])
    else:
        if K % 2 == 0:
            if abs(A[0]) > A[N-1]:
                print(abs(A[N-K]))
            else:
                print(A[K-1])
        else:
            print(A[K-1])
