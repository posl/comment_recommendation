def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    B = [0 for i in range(N+1)]
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    C = [0 for i in range(N+1)]
    for i in range(1,N+1):
        C[i] = B[i]*(B[i]-1)//2
    #print(C)
    D = sum(C)
    for i in range(N):
        print(D-C[A[i]]+(B[A[i]]-1))

if __name__ == '__main__':
    main()