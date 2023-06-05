def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    #print(A)
    #print(A[k-1])
    #print(A[:k])
    if A[k-1] == A[k]:
        print(n)
    else:
        print(k)

if __name__ == '__main__':
    main()