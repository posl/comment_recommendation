def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(N,K)
    if A[0] == 1:
        print(N-1)
        return
    if N == 1:
        print(0)
        return
    for i in range(K):
        if N % A[i] == 0:
            print(N-A[i])
            return
    for i in range(K):
        if N % A[i] == 1:
            print(N-A[i]-1)
            return
    for i in range(K):
        if N % A[i] > 1:
            print(N%A[i])
            return

if __name__ == '__main__':
    main()