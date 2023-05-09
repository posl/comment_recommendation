def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    #print(A)
    #print(A[1:])
    #print(A[:-1])
    #print(A[1:] - A[:-1])
    #print(A[1:] - A[:-1] + 1)
    #print((A[1:] - A[:-1] + 1) % M)
    #print(((A[1:] - A[:-1] + 1) % M).sum())
    print((A[1:] - A[:-1] + 1) % M)
    print(((A[1:] - A[:-1] + 1) % M).sum())
    print(((A[1:] - A[:-1] + 1) % M).sum() + A[0])
    print(((A[1:] - A[:-1] + 1) % M).sum() + A[0] - M)
    print(min(((A[1:] - A[:-1] + 1) % M).sum() + A[0], ((A[1:] - A[:-1] + 1) % M).sum() + A[0] - M))

if __name__ == '__main__':
    main()