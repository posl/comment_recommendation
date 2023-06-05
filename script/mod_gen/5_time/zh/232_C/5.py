def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(N)
    # print(M)
    # #判断是否有相同的形状
    # #1.判断是否有相同的绳子
    # for i in range(M):
    #     for j in range(M):
    #         if A[i] == C[j] and B[i] == D[j]:
    #             print('Yes')
    #             return
    #         elif A[i] == D[j] and B[i] == C[j]:
    #             print('Yes')
    #             return
    # print('No')
    #2.判断是否有相同的绳子
    #1.判断是否有相同的绳子
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print('Yes')
                return
            elif A[i] == D[j] and B[i] == C[j]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()