def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    # 1行目を固定する
    for i in range(n):
        if a[0][i] == 9:
            a[0][i] = 1
        else:
            break
    # 1行目を固定した時の最大値を求める
    for i in range(1, n):
        if a[0][i] == 9:
            a[0][i] = 1
        elif a[0][i] == 1:
            a[0][i] = 9
    # 2行目以降を固定する
    for i in range(1, n):
        for j in range(n):
            if a[i][j] == 1:
                a[i][j] = 9
            elif a[i][j] == 9:
                a[i][j] = 1
    # 答えを出力する
    for i in range(n):
        for j in range(n):
            print(a[i][j], end="")
        print()

if __name__ == '__main__':
    main()