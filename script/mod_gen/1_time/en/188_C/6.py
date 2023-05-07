def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = sorted(A, reverse=True)
    #print(B)
    C = []
    for i in range(N):
        C.append([B[2**i], 2**i])
        #print(C)
    D = sorted(C, reverse=True)
    #print(D)
    print(D[1][1])

if __name__ == '__main__':
    main()