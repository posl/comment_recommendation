def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(range(1,2**N+1))
    for i in range(N):
        for j in range(2**(N-i-1)):
            if A[B[2*j]-1] < A[B[2*j+1]-1]:
                B[j] = B[2*j+1]
            else:
                B[j] = B[2*j]
    print(B[0])

if __name__ == '__main__':
    main()