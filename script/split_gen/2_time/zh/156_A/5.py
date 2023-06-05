def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(A[0]*A[1])
    #print(A[-1]*A[-2])
    #print(A[0]*A[-1])
    #print(A[1]*A[-1])
    #print(A[0]*A[-2])
    if A[0] >= 0:
        print(A[K-1]*A[K-2])
    elif A[-1] < 0:
        if K%2 == 0:
            print(A[K-1]*A[K-2])
        else:
            print(A[K-1]*A[K-2])
    else:
        if K%2 == 0:
            print(A[K-1]*A[K-2])
        else:
            if A[0]*A[1] < A[-1]*A[-2]:
                print(A[K-1]*A[K-2])
            else:
                print(A[0]*A[1])
