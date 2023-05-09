def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # マス目を作成する
    # 1:黒, 0:白
    masu = [[0 for i in range(N)] for j in range(N)]
    # (A,B)を黒く塗る
    masu[A-1][B-1] = 1
    # max(1-A,1-B)≦ k≦ min(N-A,N-B) をみたす全ての整数 k について、(A+k,B+k) を黒く塗る。
    for k in range(max(1-A,1-B),min(N-A,N-B)+1):
        masu[A+k-1][B+k-1] = 1
    # max(1-A,B-N)≦ k≦ min(N-A,B-1) をみたす全ての整数 k について、(A+k,B-k) を黒く塗る。
    for k in range(max(1-A,B-N),min(N-A,B-1)+1):
        masu[A+k-1][B-k-1] = 1
    # 出力
    for i in range(P-1,Q):
        for j in range(R-1,S):
            if masu[i][j] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

if __name__ == '__main__':
    main()