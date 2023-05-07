def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    A.sort()
    #print(A)
    #print(A[N-1])
    for i in range(N):
        if A[2*i] != A[2*i+1]:
            print(A[2*i])
            return

if __name__ == '__main__':
    main()