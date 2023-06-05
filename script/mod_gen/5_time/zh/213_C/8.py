def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(H, W, N)
    #将A, B中的数字进行排序，得到C, D
    C = sorted(A)
    D = sorted(B)
    # print(C)
    # print(D)
    #将C, D中的数字进行重新编号，得到E, F
    E = []
    F = []
    for i in range(N):
        E.append(C.index(A[i])+1)
        F.append(D.index(B[i])+1)
    # print(E)
    # print(F)
    #将E, F中的数字进行输出，得到G, H
    G = []
    H = []
    for i in range(N):
        G.append(str(E[i]))
        H.append(str(F[i]))
    # print(G)
    # print(H)
    #将G, H中的数字进行输出，得到I
    I = []
    for i in range(N):
        I.append(G[i] + " " + H[i])
    # print(I)
    #将I中的数字进行输出
    for i in range(N):
        print(I[i])

if __name__ == '__main__':
    main()