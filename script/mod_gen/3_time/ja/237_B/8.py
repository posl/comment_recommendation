def main():
    # 1行目
    H, W = map(int, input().split())
    # 2行目以降
    A = [list(map(int, input().split())) for _ in range(H)]
    # 転置行列
    B = [[A[j][i] for j in range(H)] for i in range(W)]
    # 出力
    for i in range(W):
        print(' '.join(map(str, B[i])))

if __name__ == '__main__':
    main()