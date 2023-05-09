def main():
    # R,Cを入力
    R,C = map(int,input().split())
    # Aの行列を入力
    A = [list(map(int,input().split())) for i in range(2)]
    # AのR,Cの要素を出力
    print(A[R-1][C-1])

if __name__ == '__main__':
    main()