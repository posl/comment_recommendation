def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(K)
    #print(N)
    #print(A[K-1])
    #print(A[N-1])
    #print(A[0])
    #print(A[N-1]*A[N-2])
    #print(A[0]*A[1])
    #print(A[N-1]*A[0])
    #print(A[N-1]*A[1])
    #print(A[N-2]*A[0])
    #print(A[N-2]*A[1])
    if K <= ((N*(N-1))/2):
        if A[N-1] >= 0:
            if K == 1:
                print(A[N-1]*A[N-2])
            else:
                print(A[K-1])
        elif A[N-1] < 0:
            if K == ((N*(N-1))/2):
                print(A[0]*A[1])
            else:
                print(A[N-1]*A[0])
    elif K > ((N*(N-1))/2):
        if A[N-1] >= 0:
            print(A[N-1]*A[0])
        elif A[N-1] < 0:
            print(A[N-1]*A[1])
