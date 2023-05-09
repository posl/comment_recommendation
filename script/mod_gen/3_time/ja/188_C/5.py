def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A = [0] + A
    #print(A)
    #print(2**N)
    #print(2**(N-1))
    for i in range(1, N+1):
        for j in range(1, 2**(N-i)+1):
            #print(f"{A[2*j-1]} {A[2*j]}")
            if A[2*j-1] > A[2*j]:
                A[2*j] = 0
            else:
                A[2*j-1] = 0
    print(A.index(1))

if __name__ == '__main__':
    main()