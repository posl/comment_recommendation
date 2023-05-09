def main():
    # 1行目
    H1, W1 = map(int, input().split())
    # 2行目以降
    A = [list(map(int, input().split())) for _ in range(H1)]
    # 1行目
    H2, W2 = map(int, input().split())
    # 2行目以降
    B = [list(map(int, input().split())) for _ in range(H2)]
    # ここに処理を書く
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            # 切り出し
            C = [A[k][j:j+W2] for k in range(i, i+H2)]
            # 切り出した行列とBが一致するか
            if C == B:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()