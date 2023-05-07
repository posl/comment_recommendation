def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(len(A))
    for i in range(N):
        #print(i)
        #print(A[i])
        #print(A[i+1:])
        #print(len(set(A[i+1:])))
        if len(A) == 1:
            print(1)
        elif i == N-1:
            print(0)
        elif A[i] == A[i+1]:
            print(1)
        else:
            print(len(set(A[i+1:])))

if __name__ == '__main__':
    main()