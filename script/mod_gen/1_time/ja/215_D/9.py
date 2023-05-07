def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, M)
    #print(A)
    #print(A[0])
    #print(A[-1])
    #print(A[0] == 1)
    #print(A[-1] == M)
    #print(A[0] == 1 and A[-1] == M)
    if A[0] == 1 and A[-1] == M:
        print(0)
        exit()
    #print(A)
    #p

if __name__ == '__main__':
    main()