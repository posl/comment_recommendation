def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(A)
    #print(A[0], A[1])
    #print(A[0] ^ A[1])
    #print(A[0] ^ A[1] ^ A[2])
    #print(A[0] ^ A[1] ^ A[2] ^ A[3])
    print(A[0] ^ A[1] ^ A[2] ^ A[3])

if __name__ == '__main__':
    main()