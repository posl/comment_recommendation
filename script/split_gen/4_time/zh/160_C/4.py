def main():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    #print(K,N,A)
    #print(A[0])
    #print(A[N-1])
    #print(K-A[N-1])
    if A[0] == 0:
        print(K-A[N-1])
    else:
        print(K-A[N-1]+A[0])
