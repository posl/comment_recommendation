def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(len(A))
    #print(K)
    #print(len(A)*(len(A)-1)/2)
    #print(len(A)*(len(A)-1)/2-K)
    #print(int(len(A)*(len(A)-1)/2-K))
    #print(A[int(len(A)*(len(A)-1)/2-K)])
    print(A[int(len(A)*(len(A)-1)/2-K)])

if __name__ == '__main__':
    main()