def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    if A[0] >= 0:
        print(A[K-1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(A[N-K])
        else:
            print(A[N-K-1])
        return
    #print(A)
    #pri
