def main():
    H1,W1 = map(int,input().split())
    A = []
    for i in range(H1):
        A.append(list(map(int,input().split())))
    H2,W2 = map(int,input().split())
    B = []
    for i in range(H2):
        B.append(list(map(int,input().split())))
    #print(A)
    #print(B)
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[i+k][j+l] != B[k][l]:
                        flag = False
            if flag:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()