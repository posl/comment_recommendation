def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #K=2
    #A[0][0] A[0][1]  A[0][2]
    #A[1][0] A[1][1]  A[1][2]
    #A[2][0] A[2][1]  A[2][2]
    #A[0][0] A[0][1] A[0][2] A[0][3]
    #A[1][0] A[1][1] A[1][2] A[1][3]
    #A[2][0] A[2][1] A[2][2] A[2][3]
    #A[3][0] A[3][1] A[3][2] A[3][3]
    #A[0][0] A[0][1] A[0][2] A[0][3] A[0][4]
    #A[1][0] A[1][1] A[1][2] A[1][3] A[1][4]
    #A[2][0] A[2][1] A[2][2] A[2][3] A[2][4]
    #A[3][0] A[3][1] A[3][2] A[3][3] A[3][4]
    #A[4][0] A[4][1] A[4][2] A[4][3] A[4][4]
    #2*2の領域を作成
    B = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1] + A[i-1][j-1]
    #2*2の領域の中央値を求める
    C = []
    for i in range(K, N+1):

if __name__ == '__main__':
    main()