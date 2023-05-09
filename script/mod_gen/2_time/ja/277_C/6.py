def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 階を昇順にソート
    A, B = zip(*sorted(zip(A, B)))
    A, B = list(A), list(B)
    # はしごの上の階を取得
    up = A[-1]
    # はしごの下の階を取得
    down = B[0]
    # 上の階が下の階よりも高い場合
    if up > down:
        # 上の階を出力
        print(up)
    # 上の階が下の階よりも低い場合
    else:
        # 1を出力
        print(1)

if __name__ == '__main__':
    main()