def main():
    # H,W = map(int,input().split())
    # A = []
    # for i in range(H):
    #     A.append(list(map(int,input().split())))
    # for i in range(W):
    #     for j in range(H):
    #         print(A[j][i],end=' ')
    #     print()
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(map(int,input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        for j in range(H):
            print(B[i][j],end=' ')
        print()
