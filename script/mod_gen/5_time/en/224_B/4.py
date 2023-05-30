def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            for k in range(i+1,H):
                for l in range(j+1,W):
                    if A[i][j]+A[k][l] > A[k][j]+A[i][l]:
                        print('No')
                        return
    print('Yes')
main()
