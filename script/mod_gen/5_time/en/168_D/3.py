def main():
    N, M = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]
    #print(N, M, A, B)
    #print('Yes')
    #for i in range(2, N+1):
    #    print(i)
    n = 0
    for i in range(1, N+1):
        n = 0
        for j in range(M):
            if A[j] == i or B[j] == i:
                n += 1
        print(n)

if __name__ == '__main__':
    main()