def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H2)]
    #print(A)
    #print(B)
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            #print(i,j)
            A[i][j] = A[i][j] - B[0][0]
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != A[i][j] + B[k][l]:
                        #print(A[i+k][j+l], A[i][j] + B[k][l])
                        print('No')
                        return
    print('Yes')
    return
