def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(len(A))
    #print(K)
    #print(((N*(N-1))/(2)))
    #print(int(((N*(N-1))/(2))))
    if K <= int(((N*(N-1))/(2))):
        #print(A[K])
        print(A[K])
    else:
        print(A[K-int(((N*(N-1))/(2)))-1])
