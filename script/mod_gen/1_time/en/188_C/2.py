def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = A.copy()
    for i in range(N-1):
        for j in range(2**(N-i-1)):
            B[2*j] = max(A[2*j],A[2*j+1])
            B[2*j+1] = min(A[2*j],A[2*j+1])
        A = B.copy()
    print(A.index(min(A))+1)

if __name__ == '__main__':
    main()