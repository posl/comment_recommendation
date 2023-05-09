def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[-1]:
                B.append(A[i])
    N = len(B)
    if N == 1:
        print(0)
        exit()
    B.append(B[0]+M)
    C = []
    for i in range(N):
        C.append(B[i+1]-B[i]-1)
    C.sort()
    print(sum(C[:N-1]))

if __name__ == '__main__':
    main()